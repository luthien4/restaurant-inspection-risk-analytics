# Download only the first chunk of the full dataset, so we can test the logic safely before downloading everything.

import json
from pathlib import Path

import requests

url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

chunk_size = 50000
offset = 0

# Define the parameters for the request.
params = {"$limit": chunk_size,
          "$offset": offset,
          "$order": "inspection_id"
          }

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

print("Status code:", response.status_code)
print("Final URL:", response.url)
print("Number of records downloaded:", len(data))

if len(data) > 0:
    print("First inspection ID:", data[0]["inspection_id"])
    print("Last inspection ID:", data[-1]["inspection_id"])
else:
    print("No records were downloaded")

output_path = Path("data/raw/food_inspections_chunk_000000.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

