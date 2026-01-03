# Database Migration Instructions

The reports system has been updated with new fields (`safe_to_contact`, `affected_persons`) to support the advanced intake flow.

**IMPORTANT**: A new migration `0006` has been generated. You MUST apply it.

Run the following command in your backend environment:

```bash
# If running locally
python3 manage.py migrate reports

# If running with Docker Compose (common)
docker-compose exec backend python manage.py migrate reports
```

### Changes Applied
1.  **Backend**: 
    - `Report` model now stores `affected_persons` as a flexible JSON array.
    - `reporter` details are flattened but handled via `ReporterSerializer`.
2.  **Frontend**:
    - `ReportForm.vue` is completely rebuilt to separate Reporter vs Affected Persons.
    - Implemented provisional Intake Category logic.
    - Implemented strict inputs (Phone required, name optional).

If you see "Submission failed", check your browser console. If it says "Internal Server Error" (500), it is likely the missing migration.
