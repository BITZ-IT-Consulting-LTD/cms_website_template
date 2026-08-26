"""
Server-side export helpers for General Feedback (FeedbackMessage).

Two formats are supported, per the Aug 2026 client review:
- Single message -> PDF (generate_feedback_pdf)
- Bulk / "download all" -> CSV (write_feedback_csv), scoped to the
  currently-active status filter from the admin UI.

Missing values are always rendered as the literal string "Not provided",
never left blank, per acceptance criteria.
"""
import csv
import io

from django.utils import timezone

NOT_PROVIDED = "Not provided"


def _fmt_dt(value):
    if not value:
        return NOT_PROVIDED
    return timezone.localtime(value).strftime('%d %b %Y, %H:%M')


def feedback_status_label(message):
    if message.is_archived:
        return 'Archived'
    if message.is_processed:
        return 'Reviewed'
    return 'Pending'


def _reviewer_name(message):
    if not message.reviewed_by:
        return None
    return message.reviewed_by.get_full_name() or message.reviewed_by.username


def generate_feedback_pdf(message):
    """Return a BytesIO buffer holding a single-message PDF."""
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
        topMargin=2 * cm, bottomMargin=2 * cm,
        leftMargin=2 * cm, rightMargin=2 * cm,
        title=f"Feedback Message #{message.id}",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'FeedbackTitle', parent=styles['Title'], fontSize=18, spaceAfter=4,
    )
    label_style = ParagraphStyle(
        'FieldLabel', parent=styles['Normal'], fontName='Helvetica-Bold',
        fontSize=9, textColor=colors.HexColor('#6b7280'),
    )
    body_style = ParagraphStyle(
        'MessageBody', parent=styles['Normal'], fontSize=11, leading=15,
    )

    elements = [
        Paragraph("General Feedback", title_style),
        Paragraph(f"Message #{message.id}", styles['Normal']),
        Spacer(1, 0.6 * cm),
    ]

    reviewer_name = _reviewer_name(message)
    reviewer_line = NOT_PROVIDED
    if reviewer_name:
        reviewer_line = reviewer_name
        if message.reviewed_at:
            reviewer_line += f" ({_fmt_dt(message.reviewed_at)})"
    elif message.reviewed_at:
        reviewer_line = _fmt_dt(message.reviewed_at)

    field_rows = [
        ("Sender Name", message.name or NOT_PROVIDED),
        ("Sender Email", message.email or NOT_PROVIDED),
        ("Submitted", _fmt_dt(message.submitted_at)),
        ("Status", feedback_status_label(message)),
        ("Reviewed By", reviewer_line),
    ]

    table = Table(
        [[Paragraph(f"<b>{k}</b>", label_style), Paragraph(str(v), body_style)] for k, v in field_rows],
        colWidths=[4 * cm, 12 * cm],
    )
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#e5e7eb')),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.8 * cm))

    elements.append(Paragraph("Message", label_style))
    elements.append(Spacer(1, 0.2 * cm))
    message_text = (message.message or NOT_PROVIDED).replace('\n', '<br/>')
    elements.append(Paragraph(message_text, body_style))

    doc.build(elements)
    buffer.seek(0)
    return buffer


CSV_HEADERS = [
    'ID', 'Sender Name', 'Sender Email', 'Message', 'Submitted At',
    'Status', 'Reviewed By', 'Reviewed At',
]


def write_feedback_csv(response, queryset):
    """Write CSV rows for the given FeedbackMessage queryset into response."""
    writer = csv.writer(response)
    writer.writerow(CSV_HEADERS)
    for message in queryset:
        reviewer_name = _reviewer_name(message) or NOT_PROVIDED
        writer.writerow([
            message.id,
            message.name or NOT_PROVIDED,
            message.email or NOT_PROVIDED,
            message.message or NOT_PROVIDED,
            _fmt_dt(message.submitted_at),
            feedback_status_label(message),
            reviewer_name,
            _fmt_dt(message.reviewed_at),
        ])
    return response
