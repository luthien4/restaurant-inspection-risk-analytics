# Export Full Result Distribution

import sqlite3
from pathlib import Path
import csv

db_path = Path("database/food_inspections_full.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute(
    """
    WITH total_rows AS (
        SELECT COUNT(*) AS total_inspections
        FROM inspections
    )
    SELECT
        i.results,
        COUNT(*) AS total_by_result,
        ROUND(COUNT(*) * 100.0 / t.total_inspections, 1) AS percentage_by_result
    FROM inspections AS i
    CROSS JOIN total_rows AS t
    GROUP BY i.results, t.total_inspections;
    """
)

result_distribution = cursor.fetchall()

# Define the CSV output path
output_path_csv = Path("data/processed/full_result_distribution.csv")
output_path_csv.parent.mkdir(parents=True, exist_ok=True)

columns = [
    'result',
    'total_by_result',
    'percentage_by_result'
]

# Save the CSV file
with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(result_distribution)


print("Inspection result distribution:")
for result, count, percentage in result_distribution:
    print(f"- {result}: {count} inspections ({percentage}%)")

conn.close()