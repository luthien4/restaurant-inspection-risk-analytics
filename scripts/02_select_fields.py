import json
from pathlib import Path

###### Exercise 2 - Select Useful Fields  ######

# Define the input path for the sample JSON you created in 01_fetch_api_sample.py.
input_path = Path("data/raw/api_sample_10.json")

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

print("Number of records in the original JSON", len(data))
print("Number of records in the cleaned list", len(clean_records))
print("The first cleaned record", clean_records[0])

# Save the cleaned list as a new JSON
output_path = Path("data/processed/api_clean_records.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    json.dump(clean_records, file, indent=2)

print(f"Saved clean records to {output_path}")