# Export a full-dataset CSV showing which facility types have the highest inspection failure rates.

import sqlite3
from pathlib import Path
import csv

db_path = Path("database/food_inspections_full.sqlite")

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
    HAVING total_inspections >= 100
    ORDER BY failure_rate_pct DESC;
    """
)

facility_failure_rates = cursor.fetchall()

# Define the CSV output path
output_path_csv = Path("data/processed/full_facility_failure_rates.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)

columns = [
    'facility_type',
    'total_inspections',
    'failed_inspections',
    'failure_rate_pct'
]

# Save the CSV file
with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(facility_failure_rates)

print(f"Total exported rows: {len(facility_failure_rates)}")
print(f"Output path: {output_path_csv}")

print("Failure rate by the top-10 facility types")
for facility_type, total_inspections, failed_inspections, failure_rate_pct in facility_failure_rates[:10]:
    label = facility_type or "Unknown facility type"
    print(
        f"- {label}: {failed_inspections}/{total_inspections} failed inspections "
        f"({failure_rate_pct}%)"
    )

conn.close()
