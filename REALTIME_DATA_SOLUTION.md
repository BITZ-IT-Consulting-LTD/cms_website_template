# Real-Time Data - Root Cause & Solution

## 🎯 THE REAL PROBLEM DISCOVERED

After deep investigation, I found that **your data is NOT coming from the live external API** - it's using **hardcoded fallback values**.

### File: `sauti_cms/dashboard/sauti_helpline_client.py` (Lines 182-183)

```python
# Hard baseline fix if API returns 0
if final_cases == 0: final_cases = 39903      # ❌ HARDCODED
if total_calls == 0: total_calls = 2700172    # ❌ HARDCODED
```

---

## 📋 What's Happening:

1. **External MGLSD API structure changed**
   - Current response only returns **filtered/paginated data** (last 10 records)
   - The `dash` table only has: `['this_month', 'both', 'all', 'timestamps', '', '']`
   - No aggregate totals in the payload

2. **Your parser returns 0**
   - Looks for large numbers in `dash` table
   - Doesn't find any (only timestamps)
   - Returns `total_calls = 0` and `total_cases = 0`

3. **Hardcoded fallback kicks in** (Lines 182-183)
   - Replaces 0 with static values: 2,700,172 calls and 39,903 cases
   - **Same numbers returned FOREVER**

4. **Result: Data never changes**
   - Every API call → parser fails → fallback used → static data shown

---

## 🔍 External API Current State:

### What the API Returns Now:
```json
{
  "dash": [
    ["this_month", "both", "all", "1769893200;1770164708", "", ""]
  ],
  "cases": [],          // 0 rows (filtered)
  "clients": [...],     // 10 rows only
  "perpetrators": [...], // 10 rows only
  "calls": [...],       // 10 rows only (recent calls)
  "activities": [...]   // 10 rows only
}
```

### What's Missing:
- ❌ No aggregate totals in `dash` table
- ❌ No `stats` object
- ❌ No `summary` with counts
- ❌ Cases table is empty (filtered out)

---

## 🛠️ SOLUTION OPTIONS

### Option 1: Find the Correct API Endpoint for Totals ⭐ RECOMMENDED

The external MGLSD system likely has a dedicated endpoint for aggregate statistics that we haven't found yet.

**Action Required:**
1. Contact MGLSD technical team to get the correct API endpoint for total counts
2. OR reverse-engineer the dashboard webpage to see what API calls it makes
3. Update `BASE_URL` or add a new endpoint specifically for totals

**Possible endpoints to try:**
- `https://sauti.mglsd.go.ug/helpline/api/reports/totals`
- `https://sauti.mglsd.go.ug/helpline/api/dashboard/summary`
- Query parameter: `?view=all_time` or `?filter=none`

---

### Option 2: Count Records from Paginated Data

If no totals endpoint exists, we could:
1. Make multiple paginated API calls to get all records
2. Count them locally

**Cons:**
- Very slow (potentially thousands of API calls)
- High server load
- Not practical for real-time updates

---

### Option 3: Use Database Query Instead of API

If you have direct database access to the MGLSD helpline database:

```python
# Direct DB query (if you have access)
SELECT
    COUNT(DISTINCT call_id) as total_calls,
    COUNT(DISTINCT case_id) as total_cases
FROM helpline_data
```

---

### Option 4: Keep Hardcoded Values But Update Them Periodically

**Temporary solution until proper API is found:**

```python
# Update these values manually once per week/month based on official reports
BASELINE_CALLS = 2700172    # Updated: 2026-02-03
BASELINE_CASES = 39903      # Updated: 2026-02-03
LAST_UPDATED = "2026-02-03"

if final_cases == 0:
    final_cases = BASELINE_CASES
if total_calls == 0:
    total_calls = BASELINE_CALLS
```

**Add to response:**
```json
{
  "total_calls": 2700172,
  "data_source": "manual_baseline",
  "last_updated": "2026-02-03",
  "note": "Totals updated manually from official MGLSD reports"
}
```

---

## 🔧 IMMEDIATE FIX (Temporary)

Since we don't have access to the correct API endpoint yet, here's what I recommend:

### 1. Make the Hardcoded Fallback More Transparent

```python
# sauti_cms/dashboard/sauti_helpline_client.py

# At the top of the class
BASELINE_TOTAL_CALLS = 2700172
BASELINE_TOTAL_CASES = 39903
BASELINE_LAST_UPDATED = "2026-02-03"  # Date when these were last verified

def _transform_statistics(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
    # ... existing parsing logic ...

    # Instead of silent fallback, make it explicit
    data_source = 'live_api_deep_parsed'

    if final_cases == 0:
        final_cases = self.BASELINE_TOTAL_CASES
        data_source = 'baseline_fallback'
        logger.warning(f"Could not parse cases from API, using baseline: {final_cases}")

    if total_calls == 0:
        total_calls = self.BASELINE_TOTAL_CALLS
        data_source = 'baseline_fallback'
        logger.warning(f"Could not parse calls from API, using baseline: {total_calls}")

    return {
        'total_calls': total_calls,
        'total_cases': final_cases,
        'by_status': status_counts,
        'by_priority': priority_counts,
        'data_source': data_source,
        'baseline_date': self.BASELINE_LAST_UPDATED if data_source == 'baseline_fallback' else None,
        'api_endpoint': f'{self.BASE_URL}/api/'
    }
```

### 2. Add Warning to Frontend

```vue
<!-- sauti-frontend/src/views/ReportsInsightsPage.vue -->

<div v-if="stats.data_source === 'baseline_fallback'" class="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-6">
  <div class="flex">
    <div class="flex-shrink-0">
      <svg class="h-5 w-5 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </div>
    <div class="ml-3">
      <p class="text-sm text-yellow-700">
        <strong>Note:</strong> Live data temporarily unavailable. Showing baseline statistics last updated {{ stats.baseline_date }}.
      </p>
    </div>
  </div>
</div>
```

---

## 📊 Alternative: Web Scraping Solution

If the API truly doesn't have totals, we could scrape the dashboard webpage:

```python
def fetch_totals_from_dashboard(self) -> Optional[Dict[str, Any]]:
    """
    Scrape totals from the helpline dashboard webpage
    (Use only if API endpoint doesn't exist)
    """
    try:
        from bs4 import BeautifulSoup

        url = "https://sauti.mglsd.go.ug/helpline/dashboard"
        response = self.session.get(url, timeout=20)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find elements with total calls/cases
            # (Would need to inspect the actual HTML structure)
            total_calls_elem = soup.find(id="total_calls")
            total_cases_elem = soup.find(id="total_cases")

            if total_calls_elem and total_cases_elem:
                return {
                    'total_calls': int(total_calls_elem.text.strip().replace(',', '')),
                    'total_cases': int(total_cases_elem.text.strip().replace(',', '')),
                    'data_source': 'web_scraping'
                }
    except Exception as e:
        logger.error(f"Web scraping failed: {e}")

    return None
```

---

## ✅ RECOMMENDED NEXT STEPS

1. **Contact MGLSD Technical Team**
   - Ask for the correct API endpoint for aggregate statistics
   - Request API documentation
   - Ask if query parameters are needed (e.g., `?view=all_time`)

2. **Inspect the Live Dashboard**
   - Open https://sauti.mglsd.go.ug/helpline/
   - Open browser DevTools → Network tab
   - Look for API calls that fetch totals
   - Copy the exact endpoint and parameters used

3. **Update the Code**
   - Once correct endpoint is found, update `BASE_URL` or add new method
   - Test with live data
   - Remove hardcoded fallback values

4. **Until Then: Use Transparent Fallback**
   - Implement the "Immediate Fix" above
   - Show warning to users that live data is unavailable
   - Update baseline values weekly from official MGLSD reports

---

## 🚨 WHY SESSION ID AUTHENTICATION IS NOT THE PROBLEM

The session ID works perfectly:
- ✅ API responds with HTTP 200
- ✅ Returns valid JSON data
- ✅ No authentication errors

The problem is:
- ❌ The API endpoint we're calling doesn't return aggregate totals
- ❌ It returns filtered/paginated data (last 10 records)
- ❌ Our parser correctly returns 0 (can't find totals)
- ❌ Hardcoded fallback makes it appear like data never changes

---

## 📝 CONCLUSION

**Your real-time pipeline architecture is solid.** The problem is:

1. The external MGLSD API endpoint `/hh13feb24_2/api/` doesn't return aggregate totals
2. Your parser correctly identifies this (returns 0)
3. Hardcoded fallback hides the problem by always returning static values
4. **You need the correct API endpoint from MGLSD for aggregate statistics**

Once you have the correct endpoint, the system will work perfectly with real-time updates.

---

**Next Action:** Contact MGLSD technical team or inspect the live dashboard to find the correct API endpoint for aggregate totals.
