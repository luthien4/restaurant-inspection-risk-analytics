# Read all downloaded chunk JSON files, select the same useful fields as before, and write one full cleaned CSV.

import json
import csv
from pathlib import Path

offsets = [
    "000000",
    "050000",
    "100000",
    "150000",
    "200000",
    "250000",
    "300000"
]

columns = [
    "inspection_id",
    "dba_name",
    "facility_type",
    "risk",
    "zip",
    "inspection_date",
    "inspection_type",
    "results",
    "violations",
    "latitude",
    "longitude"
]

# Define the CSV output path
output_path_csv = Path("data/processed/food_inspections_full_clean.csv")

# Open the CSV file
with output_path_csv.open("w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=columns)
    writer.writeheader()

    chunks_processed = 0
    records_written = 0
    for chunk in offsets:
        # Define the input path for the JSON saved.
        input_path = Path(f"data/raw/food_inspections_chunk_{chunk}.json")

        # Open and load that JSON file into Python
        with input_path.open("r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # For each record, create a new dictionary containing only the fields added below.
        for item in data:
            clean_row ={"inspection_id": item.get("inspection_id"),
                                  "dba_name": item.get("dba_name"),
                                  "facility_type": item.get("facility_type"),
                                  "risk": item.get("risk"),
                                  "zip": item.get("zip"),
                                  "inspection_date": item.get("inspection_date"),
                                  "inspection_type": item.get("inspection_type"),
                                  "results": item.get("results"),
                                  "violations": item.get("violations"),
                                  "latitude": item.get("latitude"),
                                  "longitude": item.get("longitude")
                       }

            # Write the rows in the csv file.
            writer.writerow(clean_row)
            records_written += 1

        print(f"Chunk {chunk} processed")
        chunks_processed += 1


print("Total record written:", records_written)
print("Chunks processed:", chunks_processed)
print("Output path:", output_path_csv)