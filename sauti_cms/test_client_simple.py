#!/usr/bin/env python
"""
Quick test of the helpline client without Django
"""
import sys
import os

# Add the project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock Django cache for testing
class MockCache:
    def get(self, key):
        return None
    def set(self, key, value, timeout):
        pass

# Patch cache before importing
import django
from unittest.mock import Mock
sys.modules['django.core.cache'] = Mock()
sys.modules['django.core.cache'].cache = MockCache()

# Now import the client
from dashboard.sauti_helpline_client import SautiHelplineClient

def main():
    print("="*60)
    print("Testing Sauti Helpline Client")
    print("="*60)
    
    client = SautiHelplineClient()
    stats = client.fetch_case_statistics()
    
    if stats:
        print("\n✅ SUCCESS! Statistics processed:\n")
        print(f"Total Calls:          {stats['total_calls']:,}")
        print(f"Total Cases:          {stats['total_cases']:,}")
        print(f"GBV Cases:            {stats['total_gbv_cases']:,}")
        print(f"SEA Cases:            {stats['total_sea_cases']:,}")
        print(f"Migrant Workers:      {stats['total_migrant_workers']:,}")
        
        print("\n📊 By Status:")
        for status, count in stats['by_status'].items():
            print(f"  {status:15} {count:,}")
        
        print("\n🎯 By Priority:")
        for priority, count in stats['by_priority'].items():
            print(f"  {priority:15} {count:,}")
        
        print(f"\n📝 Data Source: {stats.get('data_source', 'unknown')}")
        print(f"💡 Note: {stats.get('note', 'N/A')}")
        
        print("\n" + "="*60)
        print("✅ Client is working! Your statistics page should now")
        print("   display these numbers.")
        print("="*60)
    else:
        print("\n❌ Failed to get statistics")

if __name__ == "__main__":
    main()
