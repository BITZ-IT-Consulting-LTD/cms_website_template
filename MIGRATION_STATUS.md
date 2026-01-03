# Migration Status
**SUCCESS**

I have successfully applied the pending migrations to the database inside the `sauti_backend_dev` container.

**Changes Applied:**
- `0005_historicalreport_reporting_for_report_reporting_for`: Added `reporting_for` field.
- `0006_historicalreport_affected_persons_and_more`: Added `affected_persons` and `safe_to_contact`.

**Next Steps:**
- You can now test the **Case Reporting Form** again.
- The `400 Bad Request` and `500 Server Error` issues should be resolved.
