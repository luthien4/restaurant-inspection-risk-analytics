import json
import csv
from pathlib import Path

###### Exercise 3 - Clean JSON to CSV  ######

# Define the input path for the JSON saved in 02_select_fields
input_path = Path("data/processed/api_clean_records.json")

# Open and load that JSON file into Python
with input_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

print(f"Loaded {len(data)} cleaned records")

# Define the CSV output path
output_path = Path("data/processed/api_clean_records.csv")

# Define a list of columns
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
    "longitude",
]

# Save the CSV file
with output_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader()
    writer.writerows(data)

print(f"Saved clean CSV file to {output_path}")

###################################################################################################

