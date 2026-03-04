#!/usr/bin/env python3
"""
Test Report Status Update with JWT Authentication
"""

import requests
import json

BASE_URL = "http://localhost:8001"  # Direct backend access
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

def get_jwt_token():
    """Get JWT access token"""
    print_info("Getting JWT access token...")

    try:
        response = requests.post(
            f"{BASE_URL}/api/auth/login/",
            json={
                'username': ADMIN_USERNAME,
                'password': ADMIN_PASSWORD
            },
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access')
            if access_token:
                print_success(f"  JWT token obtained")
                return access_token
            else:
                print_error("  No access token in response")
                print_info(f"  Response: {data}")
                return None
        else:
            print_error(f"  Login failed: HTTP {response.status_code}")
            print_info(f"  Response: {response.text[:200]}")
            return None
    except Exception as e:
        print_error(f"  Error: {str(e)}")
        return None

def test_report_status_update():
    """Test report status update with JWT authentication"""
    print_header("Report Status Update Test - JWT Authentication")

    # Step 1: Get JWT token
    token = get_jwt_token()
    if not token:
        print_error("Cannot proceed without authentication token")
        return False

    # Prepare headers with JWT token
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Step 2: Get reports list
    print_info("\nStep 1: Fetching reports list...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/reports/list/",
            headers=headers,
            timeout=10
        )

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
            response = requests.get(
                f"{BASE_URL}/api/reports/{report_id}/",
                headers=headers,
                timeout=10
            )

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
                    'CLOSED': 'PENDING',
                    'ESCALATED': 'RESOLVED',
                    'FORWARDED': 'RESOLVED'
                }
                new_status = status_map.get(current_status, 'IN_PROGRESS')

                print_info(f"  Changing status: {current_status} -> {new_status}")

                # Prepare update payload
                update_data = {
                    'status': new_status
                }

                # Try PATCH request
                print_info(f"  Sending PATCH request to /api/reports/{report_id}/")
                response = requests.patch(
                    f"{BASE_URL}/api/reports/{report_id}/",
                    json=update_data,
                    headers=headers,
                    timeout=10
                )

                print_info(f"  Response Status: {response.status_code}")

                if response.status_code == 200:
                    print_success("  [OK] Status update successful!")
                    try:
                        updated_report = response.json()
                        print_info(f"  New status: {updated_report.get('status')}")
                    except:
                        pass

                    # Verify the change
                    verify_response = requests.get(
                        f"{BASE_URL}/api/reports/{report_id}/",
                        headers=headers,
                        timeout=10
                    )
                    if verify_response.status_code == 200:
                        verified = verify_response.json()
                        if verified.get('status') == new_status:
                            print_success("  [OK] Verified: Status change persisted in database")

                            print_info(f"\n  All status fields:")
                            print_info(f"    status: {verified.get('status')}")
                            print_info(f"    status_display: {verified.get('status_display')}")
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
                    return False
                else:
                    print_error(f"  [FAIL] Unexpected response: {response.status_code}")
                    print_info(f"  Response: {response.text[:200]}")
                    return False
            else:
                print_error(f"  [FAIL] Could not retrieve report detail: HTTP {response.status_code}")
                return False
        elif response.status_code == 403:
            print_error("  [FAIL] Forbidden (403)")
            print_info("  User does not have Editor/Admin permissions")
            return False
        else:
            print_error(f"  [FAIL] Could not retrieve reports: HTTP {response.status_code}")
            print_info(f"  Response: {response.text[:200]}")
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
        print_success("Backend Report Status Update is WORKING correctly")
        print_info("")
        print_info("The issue reported by the user is likely:")
        print_info("  1. Frontend not using correct HTTP method (must be PATCH or PUT)")
        print_info("  2. Frontend not sending JWT token in Authorization header")
        print_info("  3. Frontend sending wrong status value format")
        print_info("  4. Frontend not handling response correctly")
        print_info("")
        print_info("Next steps:")
        print_info("  - Check frontend Vue component making the status update")
        print_info("  - Verify axios call is using PATCH method")
        print_info("  - Confirm Authorization header is included")
        print_info("  - Check browser DevTools Network tab")
    else:
        print_error("Backend Report Status Update test FAILED")
        print_info("Check the error messages above for details")

    exit(0 if success else 1)
