#!/usr/bin/env python
"""
Test script to discover the actual Sauti helpline API endpoint
Run this to find the correct URL and test connectivity
"""
import requests
import json
import sys

def test_endpoint(url, description):
    """Test a potential API endpoint"""
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"URL: {url}")
    print('='*60)
    
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Sauti-CMS-Test/1.0',
            'Accept': 'application/json'
        })
        
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'N/A')}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"✅ SUCCESS! Got JSON response")
                print(f"Response keys: {list(data.keys())}")
                
                # Check if it matches the structure you shared
                if 'cases' in data and 'cases_k' in data:
                    print("🎯 This looks like the correct endpoint!")
                    print(f"Total case rows: {len(data.get('cases', []))}")
                    
                    # Save the response for inspection
                    with open('helpline_response.json', 'w') as f:
                        json.dump(data, f, indent=2)
                    print("📝 Full response saved to: helpline_response.json")
                    return True
                else:
                    print("⚠️  JSON structure doesn't match expected format")
                    print(f"First 500 chars: {str(data)[:500]}")
                    
            except json.JSONDecodeError:
                print(f"❌ Response is not JSON")
                print(f"First 200 chars: {response.text[:200]}")
        else:
            print(f"❌ HTTP {response.status_code}")
            print(f"Response: {response.text[:200]}")
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Connection error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return False

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║         Sauti Helpline API Endpoint Discovery Tool          ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    base_url = "https://sauti.mglsd.go.ug/helpline"
    
    # List of potential API endpoints to test
    endpoints_to_test = [
        (f"{base_url}/api/stats", "Main stats API"),
        (f"{base_url}/api/v1/stats", "Versioned stats API"),
        (f"{base_url}/api/cases/stats", "Cases stats API"),
        (f"{base_url}/api/dashboard/stats", "Dashboard stats API"),
        (f"{base_url}/stats", "Direct stats endpoint"),
        (f"{base_url}/api/reports/cases", "Reports cases API"),
        (f"{base_url}/data/cases", "Data cases endpoint"),
    ]
    
    print("Testing potential API endpoints...")
    print("This may take a minute...\n")
    
    found = False
    for url, description in endpoints_to_test:
        if test_endpoint(url, description):
            found = True
            print(f"\n✅ FOUND WORKING ENDPOINT: {url}")
            print(f"\nUpdate sauti_helpline_client.py with:")
            print(f"  response = self.session.get('{url}')")
            break
    
    if not found:
        print("\n" + "="*60)
        print("❌ No working endpoint found automatically")
        print("="*60)
        print("\nNext steps:")
        print("1. Open https://sauti.mglsd.go.ug/helpline/ in Chrome")
        print("2. Press F12 → Network tab → XHR filter")
        print("3. Reload the page and look for JSON responses")
        print("4. Find the request that returns the case data")
        print("5. Copy the full URL and test it with:")
        print(f"   python {sys.argv[0]} <URL>")
        print("\nOr manually test with curl:")
        print("   curl -H 'Accept: application/json' <URL>")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Test a specific URL provided as argument
        custom_url = sys.argv[1]
        test_endpoint(custom_url, "Custom URL")
    else:
        main()
