# Verify full SQLite load with basic row-count checks.

import sqlite3
from pathlib import Path

db_path = Path("database/food_inspections_full.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT COUNT(*)
    FROM inspections;
    """
)

row_count = cursor.fetchone()

print(f"Total rows in inspections: {row_count[0]}")

cursor.execute(
    """
    SELECT
        results,
        COUNT(*)
    FROM inspections
    GROUP BY results;
    """
)

result_counts = cursor.fetchall()

print("\nRows by inspection result:")
for result, count in result_counts:
    print(f"- {result}: {count}")

conn.close()
