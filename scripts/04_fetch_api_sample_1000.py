import requests
import json
from pathlib import Path

###### Exercise 4 - API sample with 1000 rows   ######

# Define API URL
url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

# Define parameters to request 1000 rows
params = {"$limit": 1000,
          "$order": "inspection_date DESC"}

# Send the request
response = requests.get(url, params=params)
response.raise_for_status()

# Convert the JSON response to a Python list or dictionary
data = response.json()

print("Status code:", response.status_code)
print("Final URL:", response.url)
print("Number of records downloaded:", len(data))

if len(data) > 0:
    print("First inspection date", data[0].get("inspection_date"))
    print("Last inspection date", data[-1].get("inspection_date"))
else:
    print("No records were downloaded")

# 1. Create a 'Path' object representing the desired location to save the file
output_path = Path("data/raw/api_sample_1000.json")

# 2. Create the folder where the file will live. In this case, the folder part is 'data/raw'
output_path.parent.mkdir(parents=True, exist_ok=True)

print("Output path", output_path)

# 3. Open the file for writing. "w" means write mode, and encoding="utf-8" handles text characters safely.
with output_path.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print(f"Saved sample JSON to {output_path}")