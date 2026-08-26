"""
Server-side export helpers for case Reports.

Two formats, per the Aug 2026 client review:
- Single report -> PDF (generate_report_pdf), used from the report detail view.
- Bulk -> CSV (write_reports_csv), used from the reports list view.

Case-report data is sensitive: `ip_address`, `user_agent` and
`encrypted_description` are deliberately never read here, in either format.
Missing values are always rendered as the literal string "Not provided".

Note: item 12 of the Aug 2026 review (owned by a different agent) adds a few
more submission fields to the Report model — reporter alternative contact,
victim/affected-person location and a first-class `incident_type`. Those
model fields did not exist yet on this branch at the time this export was
written, so they are read defensively with getattr(..., None) below. Once
that migration lands, the corresponding row appears automatically; until
then it renders "Not provided" rather than erroring.
"""
import csv
import io

from django.utils import timezone

NOT_PROVIDED = "Not provided"


def _fmt_dt(value):
    if not value:
        return NOT_PROVIDED
    return timezone.localtime(value).strftime('%d %b %Y, %H:%M')


def _text(value):
    if value is None or value == '':
        return NOT_PROVIDED
    return value


def _bool(value):
    if value is None:
        return NOT_PROVIDED
    return 'Yes' if value else 'No'


CATEGORY_LABELS = {
    'CHILD_PROTECTION': 'Child Protection',
    'GBV': 'Gender-Based Violence',
    'MIGRANT': 'Migrant Worker',
    'PSEA': 'PSEA (Sexual Exploitation & Abuse)',
}

STATUS_LABELS = {
    'PENDING': 'Pending Review',
    'IN_PROGRESS': 'In Progress',
    'ESCALATED': 'Escalated',
    'FORWARDED': 'Forwarded to OpenCHS',
    'RESOLVED': 'Resolved',
    'CLOSED': 'Closed',
}


def _affected_persons_lines(report):
    persons = getattr(report, 'affected_persons', None) or []
    if not persons:
        return [NOT_PROVIDED]
    lines = []
    for idx, person in enumerate(persons, start=1):
        if not isinstance(person, dict):
            continue
        name = person.get('name') or NOT_PROVIDED
        age = person.get('age') or NOT_PROVIDED
        gender = person.get('gender') or NOT_PROVIDED
        location = person.get('location') or NOT_PROVIDED
        relationship = person.get('relationship') or NOT_PROVIDED
        lines.append(
            f"Person {idx}: Name: {name} | Age: {age} | Gender: {gender} | "
            f"Location: {location} | Relationship: {relationship}"
        )
    return lines or [NOT_PROVIDED]


def _attachment_value(report):
    attachment = getattr(report, 'attachment', None)
    if not attachment:
        return NOT_PROVIDED
    try:
        return attachment.name
    except Exception:
        return NOT_PROVIDED


def _report_field_rows(report):
    """Ordered (label, value) pairs for a single report, PDF + CSV share this."""
    return [
        ("Reference Number", _text(report.reference_number)),
        ("Category", CATEGORY_LABELS.get(report.category, report.category) or NOT_PROVIDED),
        ("Incident Type", _text(getattr(report, 'incident_type', None))),
        ("Status", STATUS_LABELS.get(report.status, report.status) or NOT_PROVIDED),
        ("Reporting For", _text(report.reporting_for)),
        ("Is Anonymous", _bool(report.is_anonymous)),
        ("Is Self Report", _bool(report.is_self_report)),
        ("Contact Name", _text(report.contact_name)),
        ("Contact Phone", _text(report.contact_phone)),
        ("Contact Email", _text(report.contact_email)),
        ("Alternative Contact", _text(getattr(report, 'alternative_contact', None))),
        ("Safe To Contact", _bool(report.safe_to_contact)),
        ("Location", _text(report.location)),
        ("Victim / Affected-Person Location", _text(getattr(report, 'victim_location', None))),
        ("Reported Person Age", _text(report.reported_person_age)),
        ("Reported Person Gender", _text(report.reported_person_gender)),
        ("Description", _text(report.description)),
        ("Attachment", _attachment_value(report)),
        ("Assigned To", _text(report.assigned_to.get_full_name() if report.assigned_to else None)),
        ("Notes", _text(report.notes)),
        ("Escalated At", _fmt_dt(report.escalated_at)),
        ("Forwarded To OpenCHS At", _fmt_dt(report.forwarded_to_openchs_at)),
        ("OpenCHS Case ID", _text(report.openchs_case_id)),
        ("Created At", _fmt_dt(report.created_at)),
        ("Updated At", _fmt_dt(report.updated_at)),
        ("Resolved At", _fmt_dt(report.resolved_at)),
    ]


def generate_report_pdf(report):
    """Return a BytesIO buffer holding a single-report PDF."""
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    )

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        topMargin=1.8 * cm, bottomMargin=1.8 * cm,
        leftMargin=2 * cm, rightMargin=2 * cm,
        title=f"Case Report {report.reference_number}",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'ReportTitle', parent=styles['Title'], fontSize=18, spaceAfter=4,
    )
    section_style = ParagraphStyle(
        'SectionHeading', parent=styles['Heading2'], fontSize=12,
        spaceBefore=14, spaceAfter=6, textColor=colors.HexColor('#111827'),
    )
    label_style = ParagraphStyle(
        'FieldLabel', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=9, textColor=colors.HexColor('#6b7280'),
    )
    body_style = ParagraphStyle(
        'FieldValue', parent=styles['Normal'], fontSize=10, leading=14,
    )

    elements = [
        Paragraph("Case Report", title_style),
        Paragraph(f"Reference: {report.reference_number}", styles['Normal']),
        Spacer(1, 0.5 * cm),
    ]

    def field_table(rows):
        table = Table(
            [[Paragraph(f"<b>{k}</b>", label_style), Paragraph(str(v), body_style)] for k, v in rows],
            colWidths=[5.2 * cm, 10.8 * cm],
        )
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#e5e7eb')),
        ]))
        return table

    elements.append(field_table(_report_field_rows(report)))

    elements.append(Paragraph("Affected Persons", section_style))
    # Render as simple paragraphs rather than a two-column table, since each
    # line is already a full sentence.
    for line in _affected_persons_lines(report):
        elements.append(Paragraph(line, body_style))
        elements.append(Spacer(1, 0.15 * cm))

    followups = list(report.followups.all()) if hasattr(report, 'followups') else []
    elements.append(Paragraph("Follow-ups", section_style))
    if not followups:
        elements.append(Paragraph(NOT_PROVIDED, body_style))
    else:
        for fu in followups:
            created_by = fu.created_by.get_full_name() if fu.created_by else NOT_PROVIDED
            elements.append(Paragraph(
                f"<b>{_fmt_dt(fu.created_at)}</b> by {created_by}: {fu.action_taken or NOT_PROVIDED}",
                body_style,
            ))
            elements.append(Spacer(1, 0.15 * cm))

    doc.build(elements)
    buffer.seek(0)
    return buffer


CSV_HEADERS = [
    "Reference Number", "Category", "Incident Type", "Status", "Reporting For",
    "Is Anonymous", "Is Self Report", "Contact Name", "Contact Phone",
    "Contact Email", "Alternative Contact", "Safe To Contact", "Location",
    "Victim / Affected-Person Location", "Reported Person Age",
    "Reported Person Gender", "Description", "Attachment", "Assigned To",
    "Notes", "Escalated At", "Forwarded To OpenCHS At", "OpenCHS Case ID",
    "Created At", "Updated At", "Resolved At", "Affected Persons",
]


def write_reports_csv(response, queryset):
    """Write CSV rows for the given Report queryset into response."""
    writer = csv.writer(response)
    writer.writerow(CSV_HEADERS)
    for report in queryset:
        rows = _report_field_rows(report)
        writer.writerow(
            [value for _, value in rows] + ['; '.join(_affected_persons_lines(report))]
        )
    return response
