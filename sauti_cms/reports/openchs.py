"""
OpenCHS case-forwarding scaffold.

SAFETY / STATUS
---------------
This is a SAFE SCAFFOLD only. The real OpenCHS (child helpline / MGLSD)
case-creation API spec and credentials are NOT available yet, so the actual
HTTP call below is a clearly-marked stub:

    * It is a NO-OP unless BOTH ``OPENCHS_CREATE_URL`` and ``OPENCHS_API_TOKEN``
      are configured in Django settings. When unconfigured it logs and returns
      ``None`` without raising, so a status change to FORWARDED never fails.
    * The endpoint URL, request payload shape, and authentication scheme below
      are ASSUMPTIONS and MUST be confirmed with BITZ / MGLSD before this is
      relied upon in production.

Expected (to be confirmed):
    * Endpoint:  POST ``OPENCHS_CREATE_URL``
    * Auth:      ``Authorization: Bearer <OPENCHS_API_TOKEN>``
    * Payload:   reference_number, category, description, contact_phone,
                 location, created_at
    * Response:  JSON containing the remote case id (key name TBD).
"""
import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)

# Request timeout kept small so a slow upstream can't hang the worker/thread.
_OPENCHS_TIMEOUT = 5


def forward_case_to_openchs(report):
    """Best-effort forward of a report to OpenCHS.

    Reads configuration from Django settings. If not configured, logs and
    returns ``None`` without raising. If configured, POSTs the case payload
    with a short timeout and returns the remote case id (or ``None`` on any
    failure). This function must never raise to its caller.

    Args:
        report: A ``Report`` instance being forwarded.

    Returns:
        The remote OpenCHS case id (str) on success, otherwise ``None``.
    """
    create_url = getattr(settings, 'OPENCHS_CREATE_URL', None)
    api_token = getattr(settings, 'OPENCHS_API_TOKEN', None)

    if not create_url or not api_token:
        logger.info("OpenCHS forwarding not configured; skipping remote push")
        return None

    payload = {
        'reference_number': report.reference_number,
        'category': report.category,
        'description': report.description,
        'contact_phone': report.contact_phone,
        'location': report.location,
        'created_at': report.created_at.isoformat() if report.created_at else None,
    }

    try:
        response = requests.post(
            create_url,
            json=payload,
            headers={'Authorization': f'Bearer {api_token}'},
            timeout=_OPENCHS_TIMEOUT,
        )
        response.raise_for_status()

        # Response shape is not yet confirmed with BITZ/MGLSD; try a few
        # plausible id keys, best-effort.
        try:
            data = response.json()
        except ValueError:
            data = {}

        remote_id = None
        if isinstance(data, dict):
            for key in ('case_id', 'id', 'openchs_case_id', 'reference'):
                if data.get(key):
                    remote_id = str(data[key])
                    break

        if remote_id:
            logger.info(
                f"Report {report.reference_number} forwarded to OpenCHS "
                f"(remote case id: {remote_id})"
            )
        else:
            logger.warning(
                f"Report {report.reference_number} POSTed to OpenCHS but no "
                f"case id found in response"
            )
        return remote_id

    except Exception as e:
        logger.error(
            f"Failed to forward report {report.reference_number} to OpenCHS: {e}",
            exc_info=True,
        )
        return None
