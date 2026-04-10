"""
Sauti Helpline API Client - AUTO-AUTHENTICATING VERSION
Automatically logs in and refreshes session when expired using HTTP Basic Auth
"""
import requests
import logging
from typing import Dict, Any, Optional
from django.core.cache import cache
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)

class SautiHelplineClient:
    """Client for fetching statistics from Sauti helpline system"""
    
    BASE_URL = "https://sauti.mglsd.go.ug/hh13feb24_2"
    CACHE_TIMEOUT = 60
    SESSION_CACHE_KEY = 'sauti_session_cookie'
    SESSION_CACHE_TIMEOUT = 3600  # Cache for 1 hour
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        # Disable SSL verification for government server with certificate issues
        self.session.verify = False
        # Suppress SSL warnings
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.username = 'test'
        self.password = 'p@ssw0rd'
        self.authenticated = False
        
        logger.info("=" * 60)
        logger.info("SAUTI HELPLINE CLIENT INITIALIZED")
        logger.info("=" * 60)
        logger.info("✓ Auto-authentication enabled")
        logger.info(f"✓ Username: {self.username}")
        logger.info("=" * 60)

    def authenticate(self) -> bool:
        """Automatically authenticate with Sauti helpline using HTTP Basic Auth"""

        # Check cache first
        cached_session = cache.get(self.SESSION_CACHE_KEY)
        if cached_session:
            logger.info("Attempting to restore cached session...")
            self.session.cookies.update(cached_session)
            if self._verify_session():
                logger.info("✓ Cached session is valid!")
                self.authenticated = True
                return True
            else:
                logger.info("✗ Cached session expired, will re-authenticate")
                cache.delete(self.SESSION_CACHE_KEY)

        try:
            logger.info("=" * 60)
            logger.info("AUTHENTICATING WITH SAUTI HELPLINE")
            logger.info("=" * 60)

            # Step 1: Get initial session cookie from login page
            logger.info("Step 1: Getting initial session cookie...")
            login_page_url = f"{self.BASE_URL}/helpline/"
            response = self.session.get(login_page_url, timeout=15)
            logger.info(f"  Status: {response.status_code}")
            logger.info(f"  Cookies: {list(self.session.cookies.keys())}")

            # Step 2: Authenticate using HTTP Basic Auth to /api/ endpoint
            logger.info("Step 2: Authenticating with HTTP Basic Auth...")
            api_url = f"{self.BASE_URL}/api/"

            response = self.session.post(
                api_url,
                auth=HTTPBasicAuth(self.username, self.password),
                headers={
                    'Accept': '*/*',
                    'Origin': 'https://sauti.mglsd.go.ug',
                    'Referer': 'https://sauti.mglsd.go.ug/helpline/',
                },
                timeout=15
            )

            logger.info(f"  Status: {response.status_code}")
            logger.info(f"  Cookies: {dict(self.session.cookies)}")

            # Check if we got a valid session
            session_cookie = self.session.cookies.get('HELPLINE_SESSION_ID')
            if session_cookie and response.status_code == 200:
                logger.info(f"  Session cookie: {session_cookie}")

                # Verify the session works
                if self._verify_session():
                    logger.info("=" * 60)
                    logger.info("✓✓✓ AUTHENTICATION SUCCESSFUL! ✓✓✓")
                    logger.info("=" * 60)
                    logger.info(f"✓ Session ID: {session_cookie}")
                    logger.info(f"✓ Method: HTTP Basic Auth")
                    logger.info("=" * 60)

                    # Cache the successful session
                    cache.set(self.SESSION_CACHE_KEY, dict(self.session.cookies), self.SESSION_CACHE_TIMEOUT)
                    self.authenticated = True
                    return True
                else:
                    logger.warning(f"  Got session cookie but verification failed")
            else:
                logger.warning(f"  Authentication failed - Status: {response.status_code}")

            # If we get here, authentication failed
            logger.error("=" * 60)
            logger.error("✗✗✗ AUTHENTICATION FAILED ✗✗✗")
            logger.error("=" * 60)
            logger.error("HTTP Basic Auth failed")
            logger.error("Please check credentials or contact system administrator")
            logger.error("=" * 60)
            return False

        except Exception as e:
            logger.error("=" * 60)
            logger.error(f"✗ AUTHENTICATION ERROR: {e}")
            logger.error("=" * 60)
            import traceback
            logger.error(traceback.format_exc())
            return False

    def _verify_session(self) -> bool:
        """Verify if current session is valid"""
        try:
            test_url = f"{self.BASE_URL}/api/dash/"
            params = {'dash_period': 'all', 'dash_gbv': 'both', 'dash_src': 'all'}
            
            response = self.session.get(
                test_url,
                params=params,
                timeout=10,
                headers={
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                }
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    return 'case_source' in data
                except:
                    pass
            
            return False
            
        except Exception:
            return False

    def _ensure_authenticated(self) -> bool:
        """Ensure we have valid authentication before making API calls"""
        if self.authenticated:
            if self._verify_session():
                return True
            else:
                logger.info("Session expired, re-authenticating...")
                self.authenticated = False
        
        return self.authenticate()

    def _set_filter_context(self, period: str = 'all') -> bool:
        """Set the filter context via /api/dash/ before fetching filtered data.

        The Sauti API uses session-based filtering - you must call /api/dash/
        with the desired period before calling /api/cases/ to get filtered results.

        Args:
            period: One of 'all', 'this_year', 'this_month', 'this_week'

        Returns:
            True if filter was set successfully
        """
        # Map our periods to Sauti's expected values
        period_map = {
            'all': 'all',
            'year': 'this_year',
            'month': 'this_month',
            'week': 'this_week',
        }

        dash_period = period_map.get(period, 'all')

        try:
            dash_url = f"{self.BASE_URL}/api/dash/"
            params = {
                'dash_period': dash_period,
                'dash_gbv': 'both',
                'dash_src': 'all'
            }

            response = self.session.get(
                dash_url,
                params=params,
                timeout=15,
                headers={
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                }
            )

            if response.status_code == 200:
                data = response.json()
                if 'dash' in data:
                    # Log the filter range to verify it's working
                    dash_info = data['dash'][0] if data['dash'] else []
                    date_range = dash_info[3] if len(dash_info) > 3 else 'N/A'
                    case_source = data.get('case_source', {})
                    total_cases = case_source.get('total', ['', '0 Cases'])[1] if case_source else 'N/A'
                    logger.info(f"Filter context set to: {dash_period} (range: {date_range}, total: {total_cases})")
                    return True

            logger.warning(f"Failed to set filter context: {response.status_code}")
            return False

        except Exception as e:
            logger.error(f"Error setting filter context: {e}")
            return False

    def _set_filter_context_direct(self, dash_period: str = 'all') -> bool:
        """Set the filter context directly using the dash_period value.

        Unlike _set_filter_context which maps from our period names, this
        takes the Sauti API dash_period value directly.
        """
        try:
            dash_url = f"{self.BASE_URL}/api/dash/"
            params = {
                'dash_period': dash_period,
                'dash_gbv': 'both',
                'dash_src': 'all'
            }

            response = self.session.get(
                dash_url,
                params=params,
                timeout=15,
                headers={
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                }
            )

            if response.status_code == 200:
                logger.info(f"Filter context set to: {dash_period}")
                return True

            logger.warning(f"Failed to set filter context: {response.status_code}")
            return False

        except Exception as e:
            logger.error(f"Error setting filter context: {e}")
            return False

    def _fetch_report(self, xaxis: str, title: str = 'all_cases', dash_period: str = 'all') -> Optional[Dict]:
        """Shared helper to query /api/cases/ report endpoint

        Args:
            xaxis: The field(s) to group by
            title: Report title
            dash_period: Time period filter - 'all', 'this_year', 'this_month', 'this_week'

        Note: The Sauti API uses session-based filtering that persists server-side.
        We must call /api/dash/ to set the period before every /api/cases/ call.
        """
        # CRITICAL: Set the filter context FIRST - the Sauti API filter is session-based
        # and persists server-side. Without this, we get stale data from the last filter.
        self._set_filter_context_direct(dash_period)

        params = {
            '_title': title,
            'metrics': 'case_count',
            'type': 'bar',
            'stacked': 'stacked',
            'xaxis': xaxis,
            'yaxis': '-',
            'rpt': 'case_count',
        }

        try:
            response = self.session.get(
                f"{self.BASE_URL}/api/cases/",
                params=params,
                timeout=20,
                headers={
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                }
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                logger.warning("Session expired during report fetch, re-authenticating...")
                cache.delete(self.SESSION_CACHE_KEY)
                self.authenticated = False
                if self.authenticate():
                    response = self.session.get(
                        f"{self.BASE_URL}/api/cases/",
                        params=params,
                        timeout=20,
                        headers={
                            'Accept': 'application/json',
                            'X-Requested-With': 'XMLHttpRequest',
                        }
                    )
                    if response.status_code == 200:
                        return response.json()
            logger.error(f"Report fetch failed for xaxis={xaxis}: status {response.status_code}")
        except Exception as e:
            logger.error(f"Error fetching report xaxis={xaxis}: {e}")
        return None

    def _transform_crosstab(self, raw_cases: list, top_n: int = 15) -> Dict[str, Any]:
        """Transform [[category, ^dimension, count], ...] into Chart.js stacked bar format"""

        # 1. Group by category, collecting {dimension: count}
        cat_data = {}  # {category: {dimension: count}}
        cat_totals = {}  # {category: total}
        all_dimensions = set()

        for row in raw_cases:
            if not isinstance(row, list) or len(row) < 3:
                continue
            cat = str(row[0]).strip()
            dim = str(row[1]).strip()
            try:
                count = int(float(row[2]))
            except (ValueError, TypeError):
                continue

            if not cat:
                continue

            # Strip ^ prefix from dimension labels
            dim = dim.lstrip('^') if dim else 'Unknown'
            if not dim:
                dim = 'Unknown'

            all_dimensions.add(dim)
            if cat not in cat_data:
                cat_data[cat] = {}
                cat_totals[cat] = 0
            cat_data[cat][dim] = cat_data[cat].get(dim, 0) + count
            cat_totals[cat] += count

        # 2. Sort categories by total descending, take top_n
        sorted_cats = sorted(cat_totals.items(), key=lambda x: x[1], reverse=True)[:top_n]
        labels = [cat for cat, _ in sorted_cats]

        # 3. Sort dimensions by overall total descending
        dim_totals = {}
        for cat in labels:
            for dim, count in cat_data[cat].items():
                dim_totals[dim] = dim_totals.get(dim, 0) + count
        sorted_dims = sorted(dim_totals.items(), key=lambda x: x[1], reverse=True)
        dimensions = [d for d, _ in sorted_dims]

        # 4. Build datasets (one per dimension)
        datasets = []
        for dim in dimensions:
            data = [cat_data[cat].get(dim, 0) for cat in labels]
            datasets.append({'label': dim, 'data': data})

        return {'labels': labels, 'datasets': datasets}

    def _transform_dimension_focused(self, raw_cases: list, top_categories: int = 8) -> Dict[str, Any]:
        """Transform data to show dimensions on X-axis with categories as stacked datasets.

        This produces cleaner charts where dimensions (Gender, Region, Age) are on X-axis
        and categories (Child Neglect, Sexual Violence) are stacked bars.
        """
        # 1. Group by dimension, collecting {category: count}
        dim_data = {}  # {dimension: {category: count}}
        dim_totals = {}  # {dimension: total}
        cat_totals = {}  # {category: total} for sorting

        for row in raw_cases:
            if not isinstance(row, list) or len(row) < 3:
                continue
            cat = str(row[0]).strip()
            dim = str(row[1]).strip()
            try:
                count = int(float(row[2]))
            except (ValueError, TypeError):
                continue

            if not cat or not dim:
                continue

            # Strip ^ prefix from dimension labels
            dim = dim.lstrip('^') if dim else 'Unknown'
            if not dim:
                dim = 'Unknown'

            if dim not in dim_data:
                dim_data[dim] = {}
                dim_totals[dim] = 0
            dim_data[dim][cat] = dim_data[dim].get(cat, 0) + count
            dim_totals[dim] += count
            cat_totals[cat] = cat_totals.get(cat, 0) + count

        # 2. Sort dimensions by total descending (these become X-axis labels)
        sorted_dims = sorted(dim_totals.items(), key=lambda x: x[1], reverse=True)
        # Filter out 'Unknown' if it's tiny
        sorted_dims = [(d, t) for d, t in sorted_dims if d != 'Unknown' or t > 100]
        labels = [d for d, _ in sorted_dims]

        # 3. Get top categories by total (these become stacked datasets)
        sorted_cats = sorted(cat_totals.items(), key=lambda x: x[1], reverse=True)[:top_categories]
        categories = [c for c, _ in sorted_cats]

        # 4. Build datasets (one per category)
        datasets = []
        for cat in categories:
            data = [dim_data.get(dim, {}).get(cat, 0) for dim in labels]
            datasets.append({'label': cat, 'data': data})

        return {'labels': labels, 'datasets': datasets}

    def fetch_case_statistics(self) -> Optional[Dict[str, Any]]:
        """Fetch real case statistics from report endpoints"""
        cache_key = 'sauti_helpline_stats'
        cached_data = cache.get(cache_key)
        if cached_data:
            logger.info("Returning cached statistics")
            return cached_data

        if not self._ensure_authenticated():
            logger.error("Failed to authenticate, cannot fetch statistics")
            return None

        try:
            logger.info("FETCHING CASE STATISTICS (real data)")

            # 1. Total calls from /api/calls/ (calls_ctx lives here, NOT /api/dash/)
            total_calls = 0
            calls_url = f"{self.BASE_URL}/api/calls/"
            calls_response = self.session.get(
                calls_url, timeout=20,
                headers={'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest'}
            )
            if calls_response.status_code == 200:
                calls_data = calls_response.json()
                calls_ctx = calls_data.get('calls_ctx', [])
                if calls_ctx and len(calls_ctx[0]) > 4:
                    try:
                        total_calls = int(calls_ctx[0][4])
                    except (ValueError, TypeError, IndexError):
                        total_calls = 0

            # 2. Total cases from /api/cases/?xaxis=status
            total_cases = 0
            status_data = self._fetch_report('status')
            if status_data:
                cases_ctx = status_data.get('cases_ctx', [])
                if cases_ctx and len(cases_ctx[0]) > 4:
                    try:
                        total_cases = int(cases_ctx[0][4])
                    except (ValueError, TypeError, IndexError):
                        total_cases = 0

            # 3. GBV cases from /api/cases/?xaxis=gbv_related (key="1")
            total_gbv = 0
            gbv_data = self._fetch_report('gbv_related')
            if gbv_data:
                for row in gbv_data.get('cases', []):
                    if isinstance(row, list) and len(row) >= 2 and str(row[0]).strip() == '1':
                        try:
                            total_gbv = int(float(row[1]))
                        except (ValueError, TypeError):
                            pass
                        break

            # 4. SEA/PSEA cases from /api/cases/?xaxis=is_psea (key="1")
            total_sea = 0
            sea_data = self._fetch_report('is_psea')
            if sea_data:
                for row in sea_data.get('cases', []):
                    if isinstance(row, list) and len(row) >= 2 and str(row[0]).strip() == '1':
                        try:
                            total_sea = int(float(row[1]))
                        except (ValueError, TypeError):
                            pass
                        break

            # 5. Migrant workers from /api/cases/?xaxis=reporter_nationality (non-Ugandan)
            total_migrant = 0
            nat_data = self._fetch_report('reporter_nationality')
            if nat_data:
                for row in nat_data.get('cases', []):
                    if isinstance(row, list) and len(row) >= 2:
                        label = str(row[0]).strip()
                        # Skip empty labels and Ugandan
                        if not label or label == '^Ugandan':
                            continue
                        try:
                            total_migrant += int(float(row[1]))
                        except (ValueError, TypeError):
                            continue

            logger.info(f"Stats: calls={total_calls}, cases={total_cases}, "
                        f"gbv={total_gbv}, sea={total_sea}, migrant={total_migrant}")

            stats = {
                'total_calls': total_calls,
                'total_cases': total_cases,
                'total_gbv_cases': total_gbv,
                'total_sea_cases': total_sea,
                'total_migrant_workers': total_migrant,
                'data_source': 'live_report_api',
            }

            cache.set(cache_key, stats, self.CACHE_TIMEOUT)
            return stats

        except Exception as e:
            logger.error(f"Error fetching statistics: {e}", exc_info=True)
            return None

    def _parse_case_count(self, entry: list) -> int:
        """Parse case count from ["call", "89 Cases"]"""
        if not entry or len(entry) < 2:
            return 0
        try:
            return int(entry[1].replace(' Cases', '').replace(',', '').strip())
        except:
            return 0

    def _get_period_timestamps(self, period: str) -> tuple:
        """Get the start and end timestamps for a given period.

        Returns:
            Tuple of (start_timestamp, end_timestamp) or (None, None) for 'all'
        """
        import time
        from datetime import datetime, timedelta

        if period == 'all':
            return (None, None)

        now = datetime.now()

        if period == 'year':
            start = datetime(now.year, 1, 1)
        elif period == 'month':
            start = datetime(now.year, now.month, 1)
        elif period == 'week':
            start = now - timedelta(days=now.weekday())
            start = datetime(start.year, start.month, start.day)
        else:
            return (None, None)

        return (int(start.timestamp()), int(now.timestamp()))

    def _fetch_report_with_time(self, xaxis: str, yaxis: str = 'mn') -> Optional[Dict]:
        """Fetch report with time-series data (yaxis=mn for monthly buckets)."""
        params = {
            '_title': 'all_cases',
            'metrics': 'case_count',
            'type': 'bar',
            'stacked': 'stacked',
            'xaxis': xaxis,
            'yaxis': yaxis,
            'rpt': 'case_count',
        }

        try:
            response = self.session.get(
                f"{self.BASE_URL}/api/cases/",
                params=params,
                timeout=30,
                headers={
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                }
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                logger.warning("Session expired, re-authenticating...")
                cache.delete(self.SESSION_CACHE_KEY)
                self.authenticated = False
                if self.authenticate():
                    response = self.session.get(
                        f"{self.BASE_URL}/api/cases/",
                        params=params,
                        timeout=30,
                        headers={
                            'Accept': 'application/json',
                            'X-Requested-With': 'XMLHttpRequest',
                        }
                    )
                    if response.status_code == 200:
                        return response.json()
            logger.error(f"Report fetch failed for xaxis={xaxis}: status {response.status_code}")
        except Exception as e:
            logger.error(f"Error fetching report xaxis={xaxis}: {e}")
        return None

    def _transform_with_time_filter(self, raw_cases: list, timestamps: list,
                                     start_ts: int = None, end_ts: int = None,
                                     top_categories: int = 8) -> Dict[str, Any]:
        """Transform time-series data with optional date filtering.

        Args:
            raw_cases: List of [dimension, timestamp, count] entries
            timestamps: List of available timestamp strings from cases_y
            start_ts: Start timestamp for filtering (inclusive)
            end_ts: End timestamp for filtering (inclusive)
            top_categories: Number of top categories to include
        """
        # Convert timestamp strings to integers for comparison
        valid_timestamps = set()
        if timestamps and len(timestamps) > 0:
            for ts in timestamps[0] if isinstance(timestamps[0], list) else timestamps:
                ts_int = int(ts)
                if start_ts is None or end_ts is None:
                    valid_timestamps.add(ts)
                elif start_ts <= ts_int <= end_ts:
                    valid_timestamps.add(ts)

        # Group by dimension, aggregating counts across valid timestamps
        dim_data = {}  # {dimension: {category: count}}
        dim_totals = {}
        cat_totals = {}

        for row in raw_cases:
            if not isinstance(row, list) or len(row) < 3:
                continue

            dim = str(row[0]).strip()
            ts = str(row[1]).strip()
            try:
                count = int(float(row[2]))
            except (ValueError, TypeError):
                continue

            # Skip if timestamp is outside our filter range
            if valid_timestamps and ts not in valid_timestamps:
                continue

            # Strip ^ prefix from dimension labels
            dim = dim.lstrip('^') if dim else 'Unknown'
            if not dim:
                dim = 'Unknown'

            # For this data format, dimension is the category (e.g., CENTRAL, EASTERN)
            # We want to sum across time
            if dim not in dim_data:
                dim_data[dim] = count
            else:
                dim_data[dim] += count

        # Sort dimensions by total descending
        sorted_dims = sorted(dim_data.items(), key=lambda x: x[1], reverse=True)

        # Take top dimensions (excluding Unknown if small)
        filtered_dims = [(d, t) for d, t in sorted_dims if d != 'Unknown' or t > 100]
        labels = [d for d, _ in filtered_dims[:15]]  # Limit to 15 labels
        data = [dim_data[d] for d in labels]

        # Return as single dataset (no stacking for time-filtered data)
        return {
            'labels': labels,
            'datasets': [{
                'label': 'Cases',
                'data': data
            }]
        }

    def fetch_chart_data(self, period: str = 'all') -> Optional[Dict[str, Any]]:
        """Fetch cross-tabulated chart data for 4 stacked bar charts

        Args:
            period: One of 'all', 'year', 'month', 'week'

        Strategy:
            Pass dash_period parameter directly to /api/cases/ endpoint.
            This ensures consistent stacked bar charts with category breakdown
            for all time periods.
        """
        # Create cache key with period
        cache_key = f'sauti_helpline_charts_{period}'
        cached_data = cache.get(cache_key)
        if cached_data:
            logger.info(f"Returning cached chart data for period={period}")
            return cached_data

        if not self._ensure_authenticated():
            logger.error("Failed to authenticate, cannot fetch charts")
            return None

        # Map our period names to Sauti's expected values
        period_map = {
            'all': 'all',
            'year': 'this_year',
            'month': 'this_month',
            'week': 'this_week',
        }
        dash_period = period_map.get(period, 'all')

        logger.info(f"FETCHING CHART DATA (period={period}, dash_period={dash_period})")

        try:
            if period == 'all':
                # For all-time, use dimension-focused charts WITH category breakdown
                chart_configs = {
                    'categoryBySex': 'cat_1,clients^contact_sex',
                    'categoryByRegion': 'cat_1,clients^contact_location_0',
                    'categoryByAgeGroup': 'cat_1,clients^contact_age_group',
                    'categoryByDistrict': 'cat_1,clients^contact_location_1',
                }

                charts = {}
                for key, xaxis in chart_configs.items():
                    report = self._fetch_report(xaxis, dash_period='all')
                    if report and 'cases' in report:
                        charts[key] = self._transform_dimension_focused(report['cases'])
                        logger.info(f"Chart {key}: {len(charts[key]['labels'])} dimensions, "
                                    f"{len(charts[key]['datasets'])} categories")
                    else:
                        logger.warning(f"No data for chart {key}")
                        charts[key] = {'labels': [], 'datasets': []}
            else:
                # For filtered periods, use time-series data with client-side timestamp filtering
                # This provides accurate filtered data but without category breakdown
                chart_configs = {
                    'categoryBySex': 'clients^contact_sex',
                    'categoryByRegion': 'clients^contact_location_0',
                    'categoryByAgeGroup': 'clients^contact_age_group',
                    'categoryByDistrict': 'clients^contact_location_1',
                }

                # Get timestamp range for filtering
                start_ts, end_ts = self._get_period_timestamps(period)
                logger.info(f"Period filter: start={start_ts}, end={end_ts}")

                charts = {}
                for key, xaxis in chart_configs.items():
                    report = self._fetch_report_with_time(xaxis, yaxis='mn')
                    if report and 'cases' in report:
                        timestamps = report.get('cases_y', [])
                        charts[key] = self._transform_with_time_filter(
                            report['cases'], timestamps, start_ts, end_ts
                        )
                        logger.info(f"Chart {key} (filtered): {len(charts[key]['labels'])} dimensions")
                    else:
                        logger.warning(f"No data for chart {key}")
                        charts[key] = {'labels': [], 'datasets': []}

            cache.set(cache_key, charts, self.CACHE_TIMEOUT)
            logger.info("Charts generated successfully")
            return charts

        except Exception as e:
            logger.error(f"Error fetching charts: {e}", exc_info=True)
            return None

_client_instance = None

def get_helpline_client() -> SautiHelplineClient:
    global _client_instance
    if _client_instance is None:
        _client_instance = SautiHelplineClient()
    return _client_instance