# Export Full Violation Presence by Result

import sqlite3
from pathlib import Path
import csv

db_path = Path("database/food_inspections_full.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT
        results,
        COUNT(*) AS total_inspections,
        SUM(
            CASE WHEN violations IS NOT NULL AND violations <> '' THEN 1 ELSE 0 END
        ) AS with_violations,
        SUM(
            CASE WHEN violations IS NULL OR violations = '' THEN 1 ELSE 0 END
        ) AS without_violations,
        ROUND(
            SUM(CASE WHEN violations IS NOT NULL AND violations <> '' THEN 1 ELSE 0 END)
                * 100.0 / COUNT(*),
            1
        ) AS violation_presence_pct
    FROM inspections
    GROUP BY results
    ORDER BY violation_presence_pct DESC;
    """
)

violation_presence = cursor.fetchall()

# Define the CSV output path
output_path_csv = Path("data/processed/full_violation_presence_by_result.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)

columns = [
    'results',
    'total_inspections',
    'with_violations',
    'without_violations',
    'violation_presence_pct'
]

# Save the CSV file
with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(violation_presence)

print("Total exported rows:", len(violation_presence))
print("Output path:", output_path_csv)

print("Violation-text presence by inspection result:")
for result, total_inspections, with_violations, without_violations, violation_presence_pct in violation_presence:
    print(
        f"- {result}: {with_violations}/{total_inspections} with violations "
        f"({violation_presence_pct}%), {without_violations} without violations"
    )

conn.close()