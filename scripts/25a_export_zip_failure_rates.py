from pathlib import Path
import sqlite3
import csv

db_path = Path("database/food_inspections_full.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
    SELECT zip, 
           COUNT(*) AS total_inspections,
           SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) AS failed_inspections,
           ROUND(SUM(CASE WHEN results = 'Fail' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS failure_rate_pct
    FROM inspections
    WHERE zip IS NOT NULL AND zip <> ''
    GROUP BY zip
    HAVING COUNT(*) >= 100
    ORDER BY failure_rate_pct DESC
""")

zip_failure_rates = cursor.fetchall()

# Define the CSV output path
output_path_csv = Path("data/processed/full_zip_failure_rates.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)

columns = ['zip',
           'total_inspections',
           'failed_inspections',
           'failure_rate_pct'
          ]

# Save the CSV file
with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(zip_failure_rates)

print(f"Total exported rows: {len(zip_failure_rates)}")
print(f"Output path: {output_path_csv}")

print("Top-10 ZIP codes by failure rate")
for zip_code, total_inspections, failed_inspections, failure_rate_pct in zip_failure_rates[:10]:
    label = zip_code or "Unknown zip code"
    print(
        f"- {label}: {failed_inspections}/{total_inspections} failed inspections "
        f"({failure_rate_pct}%)"
    )

conn.close()
