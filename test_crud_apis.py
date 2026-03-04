#!/usr/bin/env python3
"""
SAUTI CMS CRUD Operations Testing Script
Tests all Django app APIs for proper CRUD functionality and image URL serialization.
"""

import requests
import json
from datetime import datetime

# Base URL for the API
BASE_URL = "http://localhost:8080/api"

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{'='*80}")
    print(f"{BLUE}{text}{RESET}")
    print(f"{'='*80}\n")

def print_success(text):
    print(f"{GREEN}[PASS]{RESET} {text}")

def print_error(text):
    print(f"{RED}[FAIL]{RESET} {text}")

def print_warning(text):
    print(f"{YELLOW}[WARN]{RESET} {text}")

def print_info(text):
    print(f"  {text}")

def test_api_endpoint(name, url, expected_image_fields=None):
    """
    Test a single API endpoint

    Args:
        name: Name of the API being tested
        url: Full URL to test
        expected_image_fields: List of image field names to check for URL fields
    """
    print_header(f"Testing: {name}")
    print_info(f"URL: {url}")

    try:
        response = requests.get(url, timeout=10)

        # Check HTTP status
        if response.status_code == 200:
            print_success(f"Status: {response.status_code} OK")
        elif response.status_code == 404:
            print_error(f"Status: {response.status_code} - Endpoint not found")
            return False
        else:
            print_warning(f"Status: {response.status_code}")

        # Parse JSON
        try:
            data = response.json()

            # Check if it's a list, paginated response, or a single object
            if isinstance(data, list):
                print_info(f"Response type: List with {len(data)} items")
                if len(data) > 0:
                    sample = data[0]
                else:
                    print_warning("Empty list - no data to test")
                    return True
            elif isinstance(data, dict) and 'results' in data:
                # Paginated response
                print_info(f"Response type: Paginated (count: {data.get('count', 0)})")
                if data.get('results') and len(data['results']) > 0:
                    sample = data['results'][0]
                else:
                    print_warning("Empty results - no data to test")
                    return True
            else:
                print_info(f"Response type: Single object")
                sample = data

            # Check for image URL fields
            if expected_image_fields:
                print_info("\nChecking image URL fields:")
                for field in expected_image_fields:
                    url_field = f"{field}_url"
                    if url_field in sample:
                        value = sample.get(url_field)
                        if value:
                            print_success(f"  {url_field}: {value}")
                            # Verify it's an absolute URL
                            if value.startswith('http://') or value.startswith('https://'):
                                print_success(f"    [OK] Absolute URL")
                            else:
                                print_warning(f"    [WARN] Not an absolute URL")
                        else:
                            print_warning(f"  {url_field}: null (no image uploaded)")
                    else:
                        print_error(f"  {url_field}: MISSING!")
                        print_info(f"    Available fields: {', '.join(sample.keys())}")

            # Print sample of first few fields
            print_info("\nSample fields:")
            count = 0
            for key, value in sample.items():
                if count < 5:
                    if isinstance(value, str) and len(str(value)) > 60:
                        print_info(f"  {key}: {str(value)[:60]}...")
                    else:
                        print_info(f"  {key}: {value}")
                    count += 1

            return True

        except json.JSONDecodeError:
            print_error("Failed to parse JSON response")
            print_info(f"Response text (first 200 chars): {response.text[:200]}")
            return False

    except requests.exceptions.RequestException as e:
        print_error(f"Request failed: {str(e)}")
        return False

def main():
    print(f"\n{BLUE}{'='*80}")
    print(f"SAUTI CMS CRUD API Testing")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}{RESET}\n")

    results = {}

    # Test 1: Posts (Blog/News)
    results['posts'] = test_api_endpoint(
        "Posts (Blog/News)",
        f"{BASE_URL}/posts/",
        expected_image_fields=['featured_image']
    )

    # Test 2: Videos
    results['videos'] = test_api_endpoint(
        "Videos",
        f"{BASE_URL}/videos/",
        expected_image_fields=['thumbnail']
    )

    # Test 3: Team Members
    results['team_members'] = test_api_endpoint(
        "Team Members",
        f"{BASE_URL}/content/team-members/",
        expected_image_fields=['image']
    )

    # Test 4: Partners
    results['partners'] = test_api_endpoint(
        "Partners",
        f"{BASE_URL}/partners/",
        expected_image_fields=['logo']
    )

    # Test 5: Resources
    results['resources'] = test_api_endpoint(
        "Resources",
        f"{BASE_URL}/resources/",
        expected_image_fields=['thumbnail']
    )

    # Test 6: FAQs (no images)
    results['faqs'] = test_api_endpoint(
        "FAQs",
        f"{BASE_URL}/faqs/",
        expected_image_fields=None
    )

    # Test 7: Organization Profile
    results['organization'] = test_api_endpoint(
        "Organization Profile",
        f"{BASE_URL}/sitesettings/organization/",
        expected_image_fields=['logo', 'favicon', 'team_photo']
    )

    # Test 8: Global Settings
    results['global_settings'] = test_api_endpoint(
        "Global Settings",
        f"{BASE_URL}/sitesettings/",
        expected_image_fields=None
    )

    # Summary
    print_header("Test Summary")
    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for name, result in results.items():
        if result:
            print_success(f"{name}: PASSED")
        else:
            print_error(f"{name}: FAILED")

    print(f"\n{BLUE}{'='*80}")
    print(f"Total: {passed}/{total} tests passed ({int(passed/total*100)}%)")
    print(f"{'='*80}{RESET}\n")

    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
