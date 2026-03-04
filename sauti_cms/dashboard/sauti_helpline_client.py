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

    def _fetch_report(self, xaxis: str, title: str = 'all_cases') -> Optional[Dict]:
        """Shared helper to query /api/cases/ report endpoint"""
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
        from collections import OrderedDict

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

    def fetch_chart_data(self) -> Optional[Dict[str, Any]]:
        """Fetch cross-tabulated chart data for 4 stacked bar charts"""
        cache_key = 'sauti_helpline_charts'
        cached_data = cache.get(cache_key)
        if cached_data:
            logger.info("Returning cached chart data")
            return cached_data

        if not self._ensure_authenticated():
            logger.error("Failed to authenticate, cannot fetch charts")
            return None

        logger.info("FETCHING CHART DATA (cross-tabulated)")

        try:
            chart_configs = {
                'categoryBySex': 'cat_1,clients^contact_sex',
                'categoryByRegion': 'cat_1,clients^contact_location_0',
                'categoryByAgeGroup': 'cat_1,clients^contact_age_group',
                'categoryByDistrict': 'cat_1,clients^contact_location_1',
            }

            charts = {}
            for key, xaxis in chart_configs.items():
                report = self._fetch_report(xaxis)
                if report and 'cases' in report:
                    charts[key] = self._transform_crosstab(report['cases'])
                    logger.info(f"Chart {key}: {len(charts[key]['labels'])} categories, "
                                f"{len(charts[key]['datasets'])} dimensions")
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