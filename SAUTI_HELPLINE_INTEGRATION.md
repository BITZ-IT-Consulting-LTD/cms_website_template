# Sauti Helpline Integration Guide

## Overview

This integration connects your CMS frontend to the external Sauti helpline system at `https://sauti.mglsd.go.ug/helpline/` to display real-time statistics on your Resources & Statistics page.

## Architecture

```
External Sauti Helpline (https://sauti.mglsd.go.ug/helpline/)
    ↓
Django Backend (Proxy Layer)
    ↓
Vue Frontend (Statistics Display)
```

## Backend Components

### 1. Helpline Client (`dashboard/sauti_helpline_client.py`)

This module handles all communication with the external Sauti helpline system:

- **Fetches case statistics** from the helpline API
- **Transforms data** from the helpline format to your frontend format
- **Caches results** for 5 minutes to reduce API load
- **Handles errors** gracefully with fallback data

**Key Methods:**
- `fetch_case_statistics()` - Gets aggregated case counts
- `fetch_chart_data()` - Gets data for charts (placeholder for now)

### 2. API Endpoints (`dashboard/views.py`)

Two new endpoints have been added:

#### `/api/dashboard/helpline-stats/`
Returns aggregated statistics:
```json
{
  "total_calls": 80000,
  "total_cases": 39901,
  "total_gbv_cases": 11970,
  "total_sea_cases": 5985,
  "total_migrant_workers": 0,
  "by_status": {
    "New": 12,
    "In Progress": 10620,
    "Resolved": 26892,
    "Closed": 2368
  },
  "by_priority": {
    "Low": 9,
    "Normal": 13000,
    "High": 16223,
    "Critical": 7856
  }
}
```

#### `/api/dashboard/helpline-charts/`
Returns chart data (currently placeholder):
```json
{
  "subcategoryBySex": {...},
  "subcategoryByAge": {...},
  "subcategoryByRegion": {...},
  "subcategoryByDistrict": {...}
}
```

## Frontend Integration

### Current Implementation

Your `ResourcesPage.vue` already has the structure to display statistics. Update the data fetching to use the new endpoint:

```javascript
// In ResourcesPage.vue, update the fetchDashboardStats method:

const fetchDashboardStats = async () => {
  try {
    const response = await api.get('/dashboard/helpline-stats/')
    dashboardStats.value = response.data
  } catch (error) {
    console.error('Error fetching dashboard stats:', error)
    // Fallback to default values
    dashboardStats.value = {
      total_calls: 0,
      total_cases: 0,
      total_gbv_cases: 0,
      total_sea_cases: 0,
      total_migrant_workers: 0
    }
  }
}
```

## Important Configuration Steps

### Step 1: Identify the Actual API Endpoint

The current implementation assumes an endpoint at:
```
https://sauti.mglsd.go.ug/helpline/api/stats
```

**You need to:**
1. Inspect the network requests on the helpline dashboard
2. Find the actual endpoint URL that returns the JSON data
3. Update `BASE_URL` and endpoint paths in `sauti_helpline_client.py`

### Step 2: Handle Authentication (if required)

If the helpline API requires authentication:

```python
# In sauti_helpline_client.py, update the session headers:

def __init__(self):
    self.session = requests.Session()
    self.session.headers.update({
        'User-Agent': 'Sauti-CMS/1.0',
        'Accept': 'application/json',
        'Authorization': 'Bearer YOUR_API_TOKEN',  # Add if needed
        # Or use cookies/session auth
    })
```

### Step 3: Refine Data Mapping

The current implementation makes estimates for GBV and SEA cases. To get accurate data:

1. **Check if the API has specific filters:**
   ```python
   # Example: If there's a gbv_related field
   response = self.session.get(
       f"{self.BASE_URL}/api/cases",
       params={'gbv_related': 'true'}
   )
   ```

2. **Or parse the cases_k metadata:**
   ```python
   # The JSON you shared has a 'gbv_related' field in cases_k
   # Use this to filter cases accurately
   ```

### Step 4: Implement Chart Data Endpoints

For the charts to work, you need to:

1. Find the API endpoints that return:
   - Cases by sex
   - Cases by age group
   - Cases by region
   - Cases by district

2. Update `fetch_chart_data()` in the client:
   ```python
   def fetch_chart_data(self) -> Optional[Dict[str, Any]]:
       try:
           # Example for subcategory by sex
           sex_data = self.session.get(
               f"{self.BASE_URL}/api/cases/by-sex"
           ).json()
           
           # Transform to Chart.js format
           return {
               'subcategoryBySex': {
                   'labels': ['Male', 'Female', 'Other'],
                   'datasets': [{
                       'label': 'Cases',
                       'data': [sex_data['male'], sex_data['female'], sex_data['other']]
                   }]
               },
               # ... other charts
           }
       except Exception as e:
           logger.error(f"Error: {e}")
           return None
   ```

## Testing

### 1. Test the Backend Endpoint

```bash
# Start your Django server
cd sauti_cms
python manage.py runserver

# In another terminal, test the endpoint
curl http://localhost:8000/api/dashboard/helpline-stats/
```

### 2. Test from Frontend

```bash
# Start the Vue dev server
cd sauti-frontend
npm run dev

# Navigate to the Resources page and check the Statistics tab
```

### 3. Check Logs

```bash
# Watch Django logs for any errors
python manage.py runserver

# Look for messages like:
# "Successfully fetched and cached helpline statistics"
# or error messages if the API call fails
```

## Troubleshooting

### Issue: "Unable to fetch helpline statistics"

**Possible causes:**
1. The external API endpoint is incorrect
2. The API requires authentication
3. CORS issues (if calling from frontend directly)
4. Network/firewall blocking the request

**Solution:**
- Check Django logs for detailed error messages
- Verify the API endpoint URL
- Add authentication if required
- Use the backend proxy (which you already have)

### Issue: Statistics show zeros

**Possible causes:**
1. Data transformation logic is incorrect
2. The API response format changed
3. The cases array is empty

**Solution:**
- Add logging to see the raw API response:
  ```python
  logger.info(f"Raw API response: {response.json()}")
  ```
- Verify the data structure matches your expectations

### Issue: Slow loading

**Possible causes:**
1. External API is slow
2. Cache is not working

**Solution:**
- Increase cache timeout
- Add loading indicators in the frontend
- Consider background task for data fetching

## Next Steps

1. **Find the actual API endpoints** - Inspect the helpline dashboard network tab
2. **Update the client** with correct URLs and authentication
3. **Test thoroughly** with real data
4. **Implement chart endpoints** for visualizations
5. **Add error monitoring** (e.g., Sentry) to track API failures
6. **Set up scheduled tasks** to pre-fetch and cache data

## API Endpoint Discovery

To find the exact endpoints:

1. Open https://sauti.mglsd.go.ug/helpline/ in Chrome
2. Open DevTools (F12) → Network tab
3. Reload the page
4. Look for XHR/Fetch requests
5. Find requests that return JSON with case data
6. Note the full URL, headers, and request method
7. Update `sauti_helpline_client.py` accordingly

## Security Considerations

- **Never expose API keys** in frontend code
- **Use environment variables** for sensitive configuration
- **Implement rate limiting** to prevent abuse
- **Validate and sanitize** all data from external APIs
- **Use HTTPS** for all API communications

## Support

If you encounter issues:
1. Check Django logs: `python manage.py runserver`
2. Check browser console for frontend errors
3. Verify API endpoints are accessible
4. Test with curl or Postman first
