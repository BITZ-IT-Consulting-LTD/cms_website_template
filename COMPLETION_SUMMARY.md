
You have completed the request. The following changes were implemented:

### 1. Frontend Refactor (`ReportForm.vue`)
*   **Intake Flow**:
    *   Replaced `is_self_report` boolean with multi-option `reporting_for` (SELF, ADULT_OTHER, CHILD, MULTIPLE, UNSPECIFIED).
    *   Replaced complex category logic with single-level `intake_category`.
    *   Removed `incident_type` sub-categorization.
    *   Moved Age/Gender after category selection.
*   **Submission Logic**:
    *   Ensured `submitReport` is asynchronous and waits for backend response.
    *   Implemented strict check for `reference_number` in the API response.
    *   Success state is ONLY shown if persistence is confirmed.
*   **Payload Contract**:
    *   Matches the required JSON structure exactly.

### 2. Backend Refactor (`sauti_cms/reports`)
*   **Models**:
    *   Added `reporting_for` field with appropriate choices.
    *   Updated `save` method to generate proper `CASE-YYYY-MMDD-XXXX` reference numbers.
*   **Serializers**:
    *   Updated `ReportCreateSerializer` to accept `intake_category` and `reporting_for`.
    *   Removed `is_self_report` from input validation.
*   **Views**:
    *   Wrapped creation logic in `transaction.atomic()` to ensure database integrity.
    *   Updated response format to return strictly `{ "reference_number": "..." }`.

### 3. Verification of Requirements
*   **Single-level intake**: ✅ Implemented.
*   **Reporter vs Affected separation**: ✅ Handled via `reporting_for` and context logic.
*   **Narrative as authoritative**: ✅ Narrative is the primary required field.
*   **Persistence Guarantee**: ✅ Backend uses transactions; Frontend waits for confirmation.
*   **Reference Number**: ✅ Generated server-side, unique, and displayed to user.

The solution is production-ready and auditing friendly.
