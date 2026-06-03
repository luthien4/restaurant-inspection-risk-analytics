# Create Full SQLite Table.

import sqlite3
from pathlib import Path

output_path_db = Path("database/food_inspections_full.sqlite")
output_path_db.parent.mkdir(parents=True, exist_ok=True)

# Connect to database.
conn = sqlite3.connect(output_path_db)

# Create cursor.
cursor = conn.cursor()

cursor.execute("""
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
        )
       """)

conn.commit()

conn.close()

print("Database ready:", output_path_db)