import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def fetch_normalized_call_stats():
    """
    Fetches raw call statistics from the upstream SAUTI endpoint and
    transforms them into a semantic key-pair format for frontend use.
    """
    url = "https://sauti.mglsd.go.ug/helpline/api/wallonly/rpt"
    params = {
        'dash_period': 'today',
        'type': 'bar',
        'stacked': 'stacked',
        'xaxis': 'hangup_status_txt',
        'yaxis': 'h',
        'vector': '1',
        'rpt': 'call_count',
        'metrics': 'call_count'
    }
    
    # Target structure
    normalized = {
        "stats": {
            "calls_today": 0,
            "calls_total": 0,
            "cases_today": 0,
            "cases_total": 0,
            "cases_ongoing": 0
        },
        "calls": {}
    }
    
    try:
        logger.info(f"Fetching upstream call stats from {url}")
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # 1. Transform Stats Object
        upstream_stats = data.get('stats', {})
        if isinstance(upstream_stats, dict):
            for key in normalized["stats"].keys():
                try:
                    # Convert to integer as per requirement
                    val = upstream_stats.get(key, 0)
                    normalized["stats"][key] = int(float(val)) if val is not None else 0
                except (ValueError, TypeError):
                    normalized["stats"][key] = 0
        
        # 2. Transform Calls Array (Positional to Key-Pair)
        # Upstream format: [ ["status", "bucket", "count"], ... ]
        upstream_calls = data.get('calls', [])
        if isinstance(upstream_calls, list):
            for entry in upstream_calls:
                if isinstance(entry, list) and len(entry) >= 3:
                    status_txt = str(entry[0])
                    time_bucket = str(entry[1])
                    try:
                        count = int(float(entry[2]))
                    except (ValueError, TypeError):
                        count = 0
                        
                    if status_txt not in normalized["calls"]:
                        normalized["calls"][status_txt] = {}
                    
                    # Group by status, then by time bucket
                    normalized["calls"][status_txt][time_bucket] = count
        
        logger.info("Successfully normalized upstream call stats")
        return normalized

    except requests.exceptions.RequestException as e:
        logger.error(f"Upstream API request failed: {e}")
        return {**normalized, "error": "Upstream service unreachable"}
    except Exception as e:
        logger.error(f"Failed to normalize call stats: {e}", exc_info=True)
        return {**normalized, "error": "Internal transformation error"}
