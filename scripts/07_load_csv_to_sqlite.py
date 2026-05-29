# Load cleaned inspection records from CSV into SQLite.

import csv
import sqlite3
from pathlib import Path

csv_input = Path("data/processed/api_sample_1000_clean.csv")
db_path = Path("database/food_inspections_sample.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Clear the table before each reload to avoid duplicate rows.
cursor.execute("DELETE FROM inspections")

with csv_input.open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    inserted_rows = 0
    for row in reader:
        cursor.execute(
            """
            INSERT INTO inspections (
                inspection_id,
                dba_name,
                facility_type,
                risk,
                zip,
                inspection_date,
                inspection_type,
                results,
                violations,
                latitude,
                longitude
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """,
            (
                row.get("inspection_id"),
                row.get("dba_name"),
                row.get("facility_type"),
                row.get("risk"),
                row.get("zip"),
                row.get("inspection_date"),
                row.get("inspection_type"),
                row.get("results"),
                row.get("violations"),
                row.get("latitude"),
                row.get("longitude"),
            ),
        )
        inserted_rows += 1

conn.commit()

conn.close()

print(f"Inserted rows: {inserted_rows}")
