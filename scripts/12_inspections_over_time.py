# Analyze monthly inspection volume and failure rates.

import sqlite3
from pathlib import Path

db_path = Path("database/food_inspections_sample.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT
        SUBSTR(inspection_date, 1, 7) AS inspection_month,
        COUNT(*) AS total_inspections,
        SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) AS total_failed_inspections,
        ROUND(
            SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
            1
        ) AS failure_rate_pct
    FROM inspections
    GROUP BY SUBSTR(inspection_date, 1, 7)
    ORDER BY SUBSTR(inspection_date, 1, 7);
    """
)

monthly_summary = cursor.fetchall()

print("Monthly inspection volume and failure rate:")
for inspection_month, total_inspections, failed_inspections, failure_rate_pct in monthly_summary:
    print(
        f"- {inspection_month}: {total_inspections} inspections, "
        f"{failed_inspections} failed ({failure_rate_pct}%)"
    )

conn.close()
