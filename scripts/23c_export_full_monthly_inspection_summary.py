# Analyze monthly inspection volume and failure rates for the full dataset.

import sqlite3
from pathlib import Path
import csv

db_path = Path("database/food_inspections_full.sqlite")

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

# Define the CSV output path
output_path_csv = Path("data/processed/full_monthly_inspection_summary.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)

columns = [
    'inspection_month',
    'total_inspections',
    'failed_inspections',
    'failure_rate_pct'
]

# Save the CSV file
with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(monthly_summary)

print("Total exported rows:", len(monthly_summary))
print("Output path:", output_path_csv)

print("Monthly inspection volume and failure rate (first 5 rows):")
for inspection_month, total_inspections, failed_inspections, failure_rate_pct in monthly_summary[:5]:
    print(
        f"- {inspection_month}: {total_inspections} inspections, "
        f"{failed_inspections} failed ({failure_rate_pct}%)"
    )

print("Monthly inspection volume and failure rate (last 5 rows):")
for inspection_month, total_inspections, failed_inspections, failure_rate_pct in monthly_summary[-5:]:
    print(
        f"- {inspection_month}: {total_inspections} inspections, "
        f"{failed_inspections} failed ({failure_rate_pct}%)"
    )
conn.close()