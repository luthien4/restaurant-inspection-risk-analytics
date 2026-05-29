# Analyze inspection result distribution from SQLite.

import sqlite3
from pathlib import Path

db_path = Path("database/food_inspections_sample.sqlite")

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

print("Inspection result distribution:")
for result, count, percentage in result_distribution:
    print(f"- {result}: {count} inspections ({percentage}%)")

conn.close()
