#!/usr/bin/env python3
"""
Test script to diagnose and test Report status update issue
With authentication support
"""

import requests
import json

BASE_URL_API = "http://localhost:8080"  # Nginx proxy for API
BASE_URL_ADMIN = "http://localhost:8001"  # Direct backend for admin
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "changeme123"

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*80}")
    print(f"{text}")
    print(f"{'='*80}{RESET}\n")

def print_success(text):
    print(f"{GREEN}[PASS]{RESET} {text}")

def print_error(text):
    print(f"{RED}[FAIL]{RESET} {text}")

def print_warning(text):
    print(f"{YELLOW}[WARN]{RESET} {text}")

def print_info(text):
    print(f"  {text}")

def login_and_get_session():
    """Login to Django admin and get session cookie"""
    print_info("Authenticating with Django admin...")

    # Create a session
    session = requests.Session()

    # Get CSRF token
    try:
        response = session.get(f"{BASE_URL_ADMIN}/admin/login/", timeout=10)
        csrf_token = session.cookies.get('csrftoken')

        # Login
        login_data = {
            'username': ADMIN_USERNAME,
            'password': ADMIN_PASSWORD,
            'csrfmiddlewaretoken': csrf_token,
            'next': '/admin/'
        }

        response = session.post(
            f"{BASE_URL_ADMIN}/admin/login/",
            data=login_data,
            headers={'Referer': f"{BASE_URL_ADMIN}/admin/login/"},
            timeout=10
        )

        if response.status_code == 200 and '/admin/login/' not in response.url:
            print_success(f"  Logged in successfully as {ADMIN_USERNAME}")
            return session
        else:
            print_error(f"  Login failed - Response URL: {response.url}")
            return None
    except Exception as e:
        print_error(f"  Login error: {str(e)}")
        return None

def test_report_status_update():
    """
    Test report status update functionality with authentication
    """
    print_header("Report Status Update Test - With Authentication")

    # Step 1: Login
    session = login_and_get_session()
    if not session:
        print_error("Cannot proceed without authentication")
        return False

    # Step 2: Get list of reports
    print_info("\nStep 1: Fetching reports list...")
    try:
        response = session.get(f"{BASE_URL_ADMIN}/api/reports/list/", timeout=10)
        print_info(f"  HTTP Status: {response.status_code}")

        if response.status_code == 200:
            print_success("  Successfully retrieved reports")
            reports = response.json()

            if isinstance(reports, list):
                report_count = len(reports)
            elif isinstance(reports, dict) and 'results' in reports:
                reports = reports['results']
                report_count = len(reports)
            else:
                report_count = 0

            print_info(f"  Found {report_count} reports")

            if report_count == 0:
                print_warning("  No reports found to test with")
                print_info("  You need to create a report first through the admin or public form")
                return False

            # Get first report
            test_report = reports[0]
            print_info(f"\n  Test Report:")
            print_info(f"    ID: {test_report.get('id')}")
            print_info(f"    Reference: {test_report.get('reference_number')}")
            print_info(f"    Current Status: {test_report.get('status')} ({test_report.get('status_display')})")

            # Step 3: Get report detail
            print_info("\nStep 2: Getting report detail...")
            report_id = test_report['id']
            response = session.get(f"{BASE_URL_ADMIN}/api/reports/{report_id}/", timeout=10)

            if response.status_code == 200:
                print_success(f"  Successfully retrieved report #{report_id}")
                detail = response.json()
                current_status = detail.get('status')
                print_info(f"  Current status: {current_status}")

                # Step 4: Update status
                print_info("\nStep 3: Attempting to update report status...")

                # Choose a different status
                status_map = {
                    'PENDING': 'IN_PROGRESS',
                    'IN_PROGRESS': 'RESOLVED',
                    'RESOLVED': 'CLOSED',
                    'CLOSED': 'PENDING'
                }
                new_status = status_map.get(current_status, 'RESOLVED')

                print_info(f"  Changing status: {current_status} -> {new_status}")

                # Get CSRF token
                csrf_token = session.cookies.get('csrftoken')

                # Prepare update payload
                update_data = {
                    'status': new_status
                }

                # Try PATCH request
                print_info(f"  Sending PATCH request to /api/reports/{report_id}/")
                response = session.patch(
                    f"{BASE_URL_ADMIN}/api/reports/{report_id}/",
                    json=update_data,
                    headers={
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrf_token,
                        'Referer': f"{BASE_URL_ADMIN}/api/reports/{report_id}/"
                    },
                    timeout=10
                )

                print_info(f"  Response Status: {response.status_code}")

                if response.status_code == 200:
                    print_success("  [OK] Status update successful!")
                    updated_report = response.json()
                    print_info(f"  New status: {updated_report.get('status')}")

                    # Verify the change
                    verify_response = session.get(f"{BASE_URL_ADMIN}/api/reports/{report_id}/", timeout=10)
                    if verify_response.status_code == 200:
                        verified = verify_response.json()
                        if verified.get('status') == new_status:
                            print_success("  [OK] Verified: Status change persisted in database")
                            return True
                        else:
                            print_error(f"  [FAIL] Status not changed: still {verified.get('status')}")
                            return False
                elif response.status_code == 400:
                    print_error("  [FAIL] Bad Request (400)")
                    try:
                        error_data = response.json()
                        print_info(f"  Error details: {json.dumps(error_data, indent=2)}")
                    except:
                        print_info(f"  Response text: {response.text}")
                    return False
                elif response.status_code == 403:
                    print_error("  [FAIL] Forbidden (403) - Permission denied")
                    print_info("  User may not have Editor/Admin role")
                    return False
                elif response.status_code == 405:
                    print_error("  [FAIL] Method Not Allowed (405)")
                    print_info("  The endpoint doesn't support PATCH method")
                    print_info("  This indicates a problem with the URL routing")
                    return False
                else:
                    print_error(f"  [FAIL] Unexpected response: {response.status_code}")
                    print_info(f"  Response: {response.text[:200]}")
                    return False
            else:
                print_error(f"  [FAIL] Could not retrieve report detail: HTTP {response.status_code}")
                return False
        else:
            print_error(f"  [FAIL] Could not retrieve reports: HTTP {response.status_code}")
            if response.status_code == 403:
                print_info("  User does not have Editor/Admin permissions")
            return False
    except Exception as e:
        print_error(f"  Exception: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_report_status_update()

    print_header("Test Summary")
    if success:
        print_success("Report status update is WORKING correctly")
        print_info("The issue reported by the user may be:")
        print_info("  1. A frontend bug (not sending correct request)")
        print_info("  2. A permission issue (user not having Editor/Admin role)")
        print_info("  3. A CSRF token issue")
    else:
        print_error("Report status update test FAILED")
        print_info("Check the error messages above for details")

    exit(0 if success else 1)
