# Export monthly inspection summary metrics to CSV.

import csv
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
        SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) AS failed_inspections,
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

output_path_csv = Path("data/processed/monthly_inspection_summary.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)

columns = [
    "inspection_month",
    "total_inspections",
    "failed_inspections",
    "failure_rate_pct",
]

with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(monthly_summary)

print(f"Exported rows: {len(monthly_summary)}")
print(f"Output path: {output_path_csv}")

conn.close()
