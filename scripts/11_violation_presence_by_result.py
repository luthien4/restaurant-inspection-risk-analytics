# Analyze violation-text presence by inspection result.

import sqlite3
from pathlib import Path

db_path = Path("database/food_inspections_sample.sqlite")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT
        results,
        COUNT(*) AS total_inspections,
        SUM(
            CASE WHEN violations IS NOT NULL AND violations <> '' THEN 1 ELSE 0 END
        ) AS total_with_violations,
        SUM(
            CASE WHEN violations IS NULL OR violations = '' THEN 1 ELSE 0 END
        ) AS total_without_violations,
        ROUND(
            SUM(CASE WHEN violations IS NOT NULL AND violations <> '' THEN 1 ELSE 0 END)
                * 100.0 / COUNT(*),
            1
        ) AS violation_rate_pct
    FROM inspections
    GROUP BY results
    ORDER BY violation_rate_pct DESC;
    """
)

violation_presence = cursor.fetchall()

print("Violation-text presence by inspection result:")
for result, total_inspections, total_with_violations, total_without_violations, violation_rate_pct in violation_presence:
    print(
        f"- {result}: {total_with_violations}/{total_inspections} with violations "
        f"({violation_rate_pct}%), {total_without_violations} without violations"
    )

conn.close()
