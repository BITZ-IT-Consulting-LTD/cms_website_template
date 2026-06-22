# Quick Start: Connecting to Sauti Helpline Statistics

## What We've Built

✅ **Backend Proxy** - Django endpoints that fetch data from `https://sauti.mglsd.go.ug/helpline/`  
✅ **Data Transformation** - Converts helpline API format to your frontend format  
✅ **Frontend Integration** - ResourcesPage now calls the new endpoints  
✅ **Caching** - Results cached for 5 minutes to reduce load  

## What You Need to Do Next

### 1. Find the Actual API Endpoint (CRITICAL)

The helpline system at `https://sauti.mglsd.go.ug/helpline/` has an API that returns the JSON data you shared. You need to find the exact URL:

**Steps:**
1. Open https://sauti.mglsd.go.ug/helpline/ in Chrome
2. Press F12 to open DevTools
3. Go to the "Network" tab
4. Click "XHR" or "Fetch" filter
5. Reload the page or interact with the statistics dashboard
6. Look for requests that return JSON with case data
7. Right-click the request → Copy → Copy as cURL

**Example of what you're looking for:**
```
Request URL: https://sauti.mglsd.go.ug/helpline/api/v1/cases/stats
Method: GET
Headers:
  - Cookie: session_id=...
  - Authorization: Bearer ...
```

### 2. Update the Client Configuration

Edit `sauti_cms/dashboard/sauti_helpline_client.py`:

```python
class SautiHelplineClient:
    # UPDATE THIS with the actual endpoint you found
    BASE_URL = "https://sauti.mglsd.go.ug/helpline"
    
    def fetch_case_statistics(self):
        # UPDATE THIS with the actual API path
        response = self.session.get(
            f"{self.BASE_URL}/api/v1/cases/stats",  # ← Change this
            timeout=10
        )
```

**If authentication is required:**
```python
def __init__(self):
    self.session = requests.Session()
    self.session.headers.update({
        'User-Agent': 'Sauti-CMS/1.0',
        'Accept': 'application/json',
        'Authorization': 'Bearer YOUR_TOKEN_HERE',  # ← Add this
        # Or use cookies:
        # 'Cookie': 'session_id=YOUR_SESSION_ID'
    })
```

### 3. Test the Backend

```bash
# Terminal 1: Start Django
cd sauti_cms
python manage.py runserver

# Terminal 2: Test the endpoint
curl http://localhost:8000/api/dashboard/helpline-stats/
```

**Expected output:**
```json
{
  "total_calls": 80000,
  "total_cases": 39901,
  "total_gbv_cases": 11970,
  "total_sea_cases": 5985,
  "total_migrant_workers": 0,
  "by_status": {...},
  "by_priority": {...}
}
```

**If you see an error:**
- Check Django console for error messages
- Verify the API URL is correct
- Check if authentication is needed

### 4. Test the Frontend

```bash
# Terminal 1: Keep Django running
cd sauti_cms
python manage.py runserver

# Terminal 2: Start Vue
cd sauti-frontend
npm run dev
```

Then:
1. Open http://localhost:5173 (or your Vue dev server URL)
2. Navigate to Resources & Statistics page
3. Click the "Statistics" tab
4. Open browser console (F12)
5. Look for: "✅ Successfully loaded helpline statistics"

### 5. Refine the Data Mapping

The current implementation estimates GBV and SEA cases. To get accurate numbers:

**Option A: Use API Filters**
```python
# If the API supports filtering
gbv_response = self.session.get(
    f"{self.BASE_URL}/api/cases",
    params={'gbv_related': 'true'}
)
gbv_cases = gbv_response.json()['count']
```

**Option B: Parse the cases array**
```python
# The JSON you shared has this structure:
# cases_k has field definitions
# cases array has [final_status, priority, count]

# You can check if there's a gbv_related field and filter accordingly
for case_row in cases_data:
    # Parse based on the actual field positions
    pass
```

## Current Endpoints

Your backend now has these endpoints:

| Endpoint | Purpose | Auth Required |
|----------|---------|---------------|
| `/api/dashboard/helpline-stats/` | Get aggregated statistics | No (AllowAny) |
| `/api/dashboard/helpline-charts/` | Get chart data | No (AllowAny) |
| `/api/dashboard/stats/` | CMS internal stats | Yes (IsAuthenticated) |

## Troubleshooting

### "Unable to fetch helpline statistics"

**Check:**
1. Is the external API URL correct?
2. Does it require authentication?
3. Is there a CORS issue?
4. Check Django logs for detailed errors

**Fix:**
```bash
# Check Django logs
python manage.py runserver
# Look for error messages when you load the statistics page
```

### Statistics show all zeros

**Check:**
1. Is the data transformation logic correct?
2. Does the API response match the expected format?

**Fix:**
```python
# Add logging to see raw data
import logging
logger = logging.getLogger(__name__)

def fetch_case_statistics(self):
    response = self.session.get(...)
    raw_data = response.json()
    logger.info(f"Raw API response: {raw_data}")  # ← Add this
    # ... rest of code
```

### Charts are empty

**This is expected!** The chart endpoints are placeholders. You need to:
1. Find the chart data API endpoints
2. Implement `fetch_chart_data()` properly
3. Transform data to Chart.js format

## File Locations

```
sauti_cms/
├── dashboard/
│   ├── sauti_helpline_client.py  ← API client (UPDATE THIS)
│   ├── views.py                  ← API endpoints
│   └── urls.py                   ← URL routing

sauti-frontend/
└── src/
    └── views/
        └── ResourcesPage.vue     ← Frontend (already updated)

SAUTI_HELPLINE_INTEGRATION.md    ← Full documentation
QUICKSTART_HELPLINE.md            ← This file
```

## Next Steps Checklist

- [ ] Find the actual helpline API endpoint URL
- [ ] Update `BASE_URL` and endpoint path in `sauti_helpline_client.py`
- [ ] Add authentication if required
- [ ] Test backend endpoint with curl
- [ ] Test frontend statistics page
- [ ] Refine GBV/SEA case counting logic
- [ ] Implement chart data endpoints
- [ ] Add error monitoring (optional)
- [ ] Set up scheduled cache refresh (optional)

## Need Help?

1. **Check the logs:** Django console shows detailed error messages
2. **Use curl:** Test the API directly before integrating
3. **Browser DevTools:** Network tab shows what the helpline dashboard calls
4. **Read the full docs:** See `SAUTI_HELPLINE_INTEGRATION.md`

## Example: Complete Working Setup

Once configured, here's what happens:

1. User visits Resources & Statistics page
2. Frontend calls `/api/dashboard/helpline-stats/`
3. Django backend calls `https://sauti.mglsd.go.ug/helpline/api/...`
4. Data is transformed and cached
5. Frontend displays real statistics
6. Cache expires after 5 minutes
7. Next request fetches fresh data

**Result:** Your website shows real-time statistics from the Sauti helpline system! 🎉
