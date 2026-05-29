# Analyze inspection failure rates by facility type.

import sqlite3
from pathlib import Path

db_path = Path("database/food_inspections_sample.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT
        facility_type,
        COUNT(*) AS total_inspections,
        SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) AS failed_inspections,
        ROUND(
            SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
            1
        ) AS failure_rate_pct
    FROM inspections
    GROUP BY facility_type
    HAVING total_inspections >= 10
    ORDER BY failure_rate_pct DESC;
    """
)

facility_failure_rates = cursor.fetchall()

print("Failure rate by facility type:")
for facility_type, total_inspections, failed_inspections, failure_rate_pct in facility_failure_rates:
    label = facility_type or "Unknown facility type"
    print(
        f"- {label}: {failed_inspections}/{total_inspections} failed inspections "
        f"({failure_rate_pct}%)"
    )

conn.close()
