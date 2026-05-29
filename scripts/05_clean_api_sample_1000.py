import json
import csv
from pathlib import Path

###### Exercise 5 - API sample with 1000 rows   ######

# Define the input path for the sample JSON you created in 04_fetch_api_sample.py.
input_path = Path("data/raw/api_sample_1000.json")

# Open and load that JSON file into Python.
with input_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

clean_records = []

# For each record, create a new dictionary containing only the fields added below.
for item in data:
    clean_records.append({"inspection_id": item.get("inspection_id"),
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
                         })

# Save the cleaned list as a new JSON
output_path_json = Path("data/processed/api_sample_1000_clean.json")
output_path_json.parent.mkdir(parents=True, exist_ok=True)

with output_path_json.open("w", encoding="utf-8") as file:
    json.dump(clean_records, file, indent=2)

# Define the CSV output path
output_path_csv = Path("data/processed/api_sample_1000_clean.csv")

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
with output_path_csv.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader()

    writer.writerows(clean_records)

print("Number of raw records:", len(data))
print("Number of cleaned records:", len(clean_records))
print("JSON output path:", output_path_json)
print("CSV output path:", output_path_csv)