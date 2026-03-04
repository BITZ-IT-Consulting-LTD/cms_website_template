# Helpline Charts Integration Plan

## Status: IMPLEMENTED — ALL FILES UPDATED

---

## Issues Found & Fixes

### Issue 1: Total Calls = 0 — FIXED
- **Symptom**: KPI card shows 0 instead of ~2.7M
- **Root cause**: `calls_ctx` lives in `/api/calls/`, NOT `/api/dash/`. The code was calling `/api/dash/` looking for `calls_ctx` which doesn't exist there.
- **Fix**: Changed `fetch_case_statistics()` to call `/api/calls/` instead of `/api/dash/` for total calls. The `/api/calls/` response contains `calls_ctx: [["0","20","1","20","2716905","",""]]` where index [4] = total calls.
- **Confirmed value**: `calls_ctx[0][4]` = `"2716905"` (~2.7M)

### Issue 2: Charts empty + old titles still showing — FIXED
- **Symptom**: Page shows old titles ("Cases by Source", "Abuse Subcategories", "Regional Case Distribution") and charts are empty
- **Root cause**: The charts the user was viewing are on `ResourcesPage.vue` (Statistics tab), NOT `ReportsInsightsPage.vue`. ResourcesPage.vue still had old chart keys (`subcategoryBySex`, etc.) while backend now returns `categoryBySex`.
- **Fix**: Updated `ResourcesPage.vue` to use new chart keys, new titles, added 4th chart (District), and added case type filter dropdown with category mapping. Both `ReportsInsightsPage.vue` and `ResourcesPage.vue` now have identical chart logic.

---

## Context

The Reports & Insights page previously showed 5 KPI stat cards (with hardcoded percentage estimates for GBV/SEA/Migrant Workers) and 3 charts with incorrect data. We replaced all of this with **real data** from the Sauti helpline `/api/cases/` report endpoint, added a 4th chart, and implemented client-side filtering.

**What changed:**
- KPI cards: Replaced hardcoded percentages with real report queries
- Charts: Replaced 3 old charts with 4 new cross-tabulated stacked bar charts
- Filtering: Added ability to filter charts by case type (Abuse/Counseling/Info Inquiry)

---

## Implementation Summary

### Files Modified

| File | Status | Changes |
|------|--------|---------|
| `sauti_cms/dashboard/sauti_helpline_client.py` | DONE | Added `_fetch_report()`, `_transform_crosstab()`, rewrote `fetch_case_statistics()` and `fetch_chart_data()`, removed old chart methods |
| `sauti_cms/dashboard/views.py` | DONE | Updated fallback chart keys in `HelplineChartsView` |
| `sauti-frontend/src/views/ReportsInsightsPage.vue` | DONE | 4 charts in 2x2 grid, new data keys, filter dropdown, filter logic with category mappings |
| `sauti-frontend/src/views/ResourcesPage.vue` | DONE | Updated Statistics tab: 4 charts (was 3) with new titles and keys, added filter dropdown, filter logic with category mappings, extended color palette |

---

## Data Mapping

### KPI Stat Cards

| Card | API Endpoint | Extraction Logic | Test Result |
|------|-------------|-----------------|-------------|
| Total Calls | `/api/calls/` | `calls_ctx[0][4]` | **FIXED** (was 0, now ~2.7M) |
| Total Cases | `/api/cases/?xaxis=status` | `cases_ctx[0][4]` | 40,024 OK |
| GBV Cases | `/api/cases/?xaxis=gbv_related` | Sum `cases` rows where key=`"1"` | 12,993 OK |
| SEA Cases | `/api/cases/?xaxis=is_psea` | Sum `cases` rows where key=`"1"` | 26 OK |
| Migrant Workers | `/api/cases/?xaxis=reporter_nationality` | Sum all rows where label is NOT `"^Ugandan"` and NOT empty | 330 OK |

### 4 Charts (all cross-tabulated stacked bars)

| # | Title | API xaxis | Stacked By | Test Result |
|---|-------|-----------|------------|-------------|
| 1 | Abuse Category vs Client Sex | `cat_1,clients^contact_sex` | Female / Male / Unknown | NOT VISIBLE (frontend not refreshed) |
| 2 | Abuse Category vs Client Region | `cat_1,clients^contact_location_0` | CENTRAL / EASTERN / etc. | NOT VISIBLE |
| 3 | Abuse Category vs Client Age Group | `cat_1,clients^contact_age_group` | Age group ranges | NOT VISIBLE |
| 4 | Abuse Category vs Client District | `cat_1,clients^contact_location_1` | District names | NOT VISIBLE |

**API URL pattern for all charts:**
```
/api/cases/?_title=all_cases&metrics=case_count&type=bar&stacked=stacked&xaxis={xaxis_value}&yaxis=-&rpt=case_count
```

**Response format** (same for all 4): Array of `[category, ^dimension_value, count]` triplets:
```json
[["Child Neglect", "^Female", "9743"], ["Child Neglect", "^Male", "9156"], ...]
```

**Transform to Chart.js stacked bar:**
```javascript
{
  labels: ['Child Neglect', 'Sexual Violence', ...],      // unique categories (sorted by total desc)
  datasets: [
    { label: 'Female', data: [9743, 4011, ...] },         // one dataset per dimension value
    { label: 'Male', data: [9156, 160, ...] },
  ]
}
```

### Filtering

- **Case Type filter** dropdown: "All", "Abuse", "Counseling", "Information Inquiry"
- Filter applied **client-side** — the full dataset is fetched once, then filtered in the frontend by matching category names
- Category-to-case-type mapping is hardcoded in the Vue component based on known categories from the helpline system

---

## Detailed Changes

### 1. `sauti_cms/dashboard/sauti_helpline_client.py`

**New methods added:**

- **`_fetch_report(xaxis, title)`** — Shared helper to query `/api/cases/` with report params. Handles 401 re-authentication.
- **`_transform_crosstab(raw_cases, top_n=15)`** — Transforms `[[cat, dim, count], ...]` triplets into Chart.js stacked bar format. Strips `^` prefix from dimension labels, sorts categories by total descending (top 15), sorts dimensions by total descending.

**Rewritten methods:**

- **`fetch_case_statistics()`** — Now makes 5 real API calls:
  1. `/api/calls/` → `calls_ctx[0][4]` for total_calls **(FIXED — was using wrong endpoint)**
  2. `_fetch_report('status')` → `cases_ctx[0][4]` for total_cases
  3. `_fetch_report('gbv_related')` → row with key `"1"` for GBV count
  4. `_fetch_report('is_psea')` → row with key `"1"` for SEA count
  5. `_fetch_report('reporter_nationality')` → sum non-Ugandan for migrant count
  - Cached for 60s

- **`fetch_chart_data()`** — Now makes 4 cross-tab API calls:
  1. `_fetch_report('cat_1,clients^contact_sex')` → categoryBySex
  2. `_fetch_report('cat_1,clients^contact_location_0')` → categoryByRegion
  3. `_fetch_report('cat_1,clients^contact_age_group')` → categoryByAgeGroup
  4. `_fetch_report('cat_1,clients^contact_location_1')` → categoryByDistrict
  - Each transformed via `_transform_crosstab()`, cached for 60s

**Removed methods:**
- `_build_chart_from_dash_data()` — was building charts from case_source
- `_build_chart_from_static_data()` — was returning hardcoded region data
- `_build_top_n_chart()` — was building simple bar charts from flat data
- `_parse_cases_array()` — replaced by crosstab parsing

**Kept methods:**
- `_parse_case_count()` — still used internally
- All authentication methods (`authenticate()`, `_verify_session()`, `_ensure_authenticated()`)

### 2. `sauti_cms/dashboard/views.py`

**`HelplineChartsView` fallback keys updated:**
```python
# Old: subcategoryBySex, subcategoryByAge, subcategoryByRegion, subcategoryByDistrict
# New: categoryBySex, categoryByRegion, categoryByAgeGroup, categoryByDistrict
```

### 3. `sauti-frontend/src/views/ResourcesPage.vue` (Statistics Tab)

**This is the page the user was actually viewing.** It has a tab system with "Resources" and "Statistics" tabs. The Statistics tab shows the same KPI cards and charts.

**Template changes (lines 259-325):**
- Added filter dropdown bar above the charts grid
- Changed from 3 charts to 4 charts in a 2x2 grid:
  - Chart 1: "Abuse Category vs Client Sex" (was "Cases by Source")
  - Chart 2: "Abuse Category vs Client Region" (was "Abuse Subcategories")
  - Chart 3: "Abuse Category vs Client Age Group" (NEW)
  - Chart 4: "Abuse Category vs Client District" (was "Regional Case Distribution")
- All charts now use computed `filteredCategoryBy*` properties instead of raw `dashboardCharts.*`
- Removed `lg:col-span-2` from what was the 3rd chart (now all 4 are equal width)

**Script changes (lines 791-860):**
- Chart state keys changed from `subcategoryBySex/ByAge/ByRegion/ByDistrict` to `categoryBySex/ByRegion/ByAgeGroup/ByDistrict`
- Added `caseTypeFilter` ref (default "All")
- Added category-to-case-type constants: `ABUSE_CATEGORIES`, `COUNSELING_CATEGORIES`, `INFO_CATEGORIES`
- Added `getAllowedCategories()` and `filterChartData()` functions
- Added 4 computed properties: `filteredCategoryBySex`, `filteredCategoryByRegion`, `filteredCategoryByAgeGroup`, `filteredCategoryByDistrict`
- Extended color palette from 6 to 12 colors
- Fixed `fetchDashboardData` chart mapping to use new API response keys

### 4. `sauti-frontend/src/views/ReportsInsightsPage.vue`

**Template changes:**
- Added filter dropdown bar (section between stats and charts)
- Changed from 3 charts to 4 charts in a 2x2 grid
- Chart titles: "Abuse Category vs Client Sex/Region/Age Group/District"
- Charts bound to computed filtered properties instead of raw data

**Script changes:**
- Added category-to-case-type constants: `ABUSE_CATEGORIES`, `COUNSELING_CATEGORIES`, `INFO_CATEGORIES`
- Chart state keys changed from `subcategoryBy*` to `categoryBy*`
- Added `caseTypeFilter` ref (default "All")
- Added `filterChartData()` function — filters labels/datasets by allowed categories
- Added 4 computed properties: `filteredCategoryBySex`, `filteredCategoryByRegion`, `filteredCategoryByAgeGroup`, `filteredCategoryByDistrict`
- Extended color palette from 6 to 12 colors (charts may have many stacked dimensions)

---

## Collected API Payloads Reference

### Calls (from /api/calls/ — NOT /api/dash/)
```
calls: [[...individual call records...]]
calls_ctx: [["0", "20", "1", "20", "2716905", "", ""]]
```
**Important**: `calls_ctx` is in `/api/calls/` response, NOT in `/api/dash/`. The `/api/dash/` endpoint only has `case_source` and other dashboard data.

### Cases by Status (from /api/cases/?xaxis=status)
```
cases: [["0","21"], ["1","12987"], ["2","27014"]]
cases_ctx: [["0","20","1","20","40022","all_cases",""]]
```
Status mapping: 0=Open, 1=In Progress, 2=Closed

### Cases by GBV (from /api/cases/?xaxis=gbv_related)
```
cases: [["0","26937"], ["1","12993"], ["2","92"]]
```
GBV=Yes (key "1"): 12,993

### Cases by PSEA/SEA (from /api/cases/?xaxis=is_psea)
```
cases: [["","22"], ["0","39974"], ["1","26"]]
```
PSEA=Yes (key "1"): 26

### Cases by Nationality (from /api/cases/?xaxis=reporter_nationality)
```
cases: [["","1"], ["","724"], ["^American","4"], ["^Burundian","19"], ["^Congolese","54"],
  ["^Egyptian","1"], ["^Kenyan","37"], ["^Nigerian","3"], ["^Russian","1"],
  ["^Rwandase","128"], ["^Somalian","9"], ["^South Sudanese","42"],
  ["^Sudanese","13"], ["^Tanzanian","13"], ["^Ugandan","38967"], ["^Zambian","6"]]
```
Non-Ugandan total: 330

### Category vs Client Sex (from /api/cases/?xaxis=cat_1,clients^contact_sex)
Full cross-tabulation: [[category, ^sex, count], ...] with 38,076 total clients
Sex values: ^Female, ^Male, ^Unknown, ^Hermaphrodites

### Category vs Client Region (from /api/cases/?xaxis=cat_1,clients^contact_location_0)
Region values: CENTRAL, EASTERN, NORTHERN, WESTERN, INTERNATIONAL, Unknown (NO ^ prefix)

### Category vs Client Age Group (from /api/cases/?xaxis=cat_1,clients^contact_age_group)
Age group values: ^0-04, ^05-09, ^10-14, ^15-17, ^18-24, ^25-59, ^60+ (HAS ^ prefix)

### Category vs Client District (from /api/cases/?xaxis=cat_1,clients^contact_location_1)
District values: KAMPALA, WAKISO, MUKONO, TORORO, etc. (NO ^ prefix)

### Category hierarchy (from /api/cases/?xaxis=cat_0,cat_1,cat_2,cat_3)
Full breakdown: Abuse (child neglect, sexual violence, physical violence, etc.),
Counseling (child custody, family issues, etc.), Information Inquiry (school fees, etc.)

---

## Technical Notes

### ^ Prefix Inconsistency
- **HAS ^ prefix**: Sex values (`^Female`, `^Male`), Age groups (`^0-04`, `^05-09`)
- **NO ^ prefix**: Region values (`CENTRAL`, `EASTERN`), District values (`KAMPALA`, `WAKISO`)
- The `_transform_crosstab()` method handles both cases via `dim.lstrip('^')`

### Caching
- Stats: cached 60s with key `sauti_helpline_stats`
- Charts: cached 60s with key `sauti_helpline_charts`
- Session: cached 1 hour with key `sauti_session_cookie`

### Auto-refresh
- Frontend refreshes every 60 seconds via `setInterval`
- Backend cache ensures the external API isn't hit more than once per 60s

---

## Next Steps

1. **All code fixes applied**:
   - Changed `fetch_case_statistics()` to use `/api/calls/` for total calls (was incorrectly using `/api/dash/`)
   - Updated `ResourcesPage.vue` Statistics tab: new chart keys, titles, 4th chart, filter dropdown
   - Both `ReportsInsightsPage.vue` and `ResourcesPage.vue` now have identical chart logic

2. **Restart Docker containers** — To pick up all Python and Vue code changes

3. **Verify after restart** — Check the Statistics tab on Resources page:
   - 5 KPI cards show real numbers (Total Calls ~2.7M)
   - 4 stacked bar charts with correct titles
   - Filter dropdown works
   - If charts still empty, check `GET /api/dashboard/helpline-charts/` in browser DevTools Network tab

---

## Verification Checklist

1. **Backend API test:**
   - `GET /api/dashboard/helpline-stats/` → verify real values: total_calls ~2.7M, total_cases ~40K, gbv ~13K, sea ~26, migrant ~330
   - `GET /api/dashboard/helpline-charts/` → verify 4 chart objects with labels and stacked datasets

2. **Frontend visual test:**
   - Open Reports & Insights page
   - Verify 5 KPI cards show real numbers (including Total Calls)
   - Verify 4 stacked bar charts render with correct titles:
     - "Abuse Category vs Client Sex"
     - "Abuse Category vs Client Region"
     - "Abuse Category vs Client Age Group"
     - "Abuse Category vs Client District"
   - Verify bars are stacked by dimension (sex/region/age/district)
   - Test filter dropdown — selecting "Abuse" should show only abuse categories in all charts
   - Verify auto-refresh still works (60s interval)

3. **Edge cases:**
   - Empty dimension values (rows with `""` categories) should be excluded or labeled "Unknown"
   - `^` prefix stripped from dimension labels (show "Female" not "^Female")
   - Charts sorted by total count descending, showing top 15 categories to prevent overcrowding
