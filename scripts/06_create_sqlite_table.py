# Create the SQLite inspections table for the cleaned API sample.

import sqlite3
from pathlib import Path

output_path = Path("database/food_inspections_sample.sqlite")
output_path.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(output_path)

cursor = conn.cursor()

# IF NOT EXISTS keeps the script rerunnable while learning and iterating.
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS inspections (
        inspection_id TEXT,
        dba_name TEXT,
        facility_type TEXT,
        risk TEXT,
        zip TEXT,
        inspection_date TEXT,
        inspection_type TEXT,
        results TEXT,
        violations TEXT,
        latitude TEXT,
        longitude TEXT
    );
    """
)

conn.commit()

conn.close()

print(f"Database ready: {output_path}")

