
import requests
import json
from pathlib import Path

###### Exercise 1 - API and JSON  ######

# Define API URL
url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

# Define parameters to request only 10 rows
params = {"$limit": 10}

# Send the request
response = requests.get(url, params=params)
response.raise_for_status()

print("Status Code", response.status_code)
print("Final URL:", response.url)

# Convert the JSON response to a Python list or dictionary
data = response.json()

print("Type of data:", type(data))
print("Number of records", len(data))

if len(data) > 0:
    print("Keys of the first record", data[0].keys())

# -----------------------------------------------------------------------------------
# Save the API response, which is stored in 'data', into a JSON file on your computer.

# 1. Create a 'Path' object representing the desired location to save the file
output_path = Path("data/raw/api_sample_10.json")

# 2. Create the folder where the file will live. In this case, the folder part is 'data/raw'
output_path.parent.mkdir(parents=True, exist_ok=True)

# 3. Open the file for writing. "w" means write mode, 'encoding="utf-8" tells Python how to handle text characters safely'
with output_path.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print(f"Saved sample JSON to {output_path}")