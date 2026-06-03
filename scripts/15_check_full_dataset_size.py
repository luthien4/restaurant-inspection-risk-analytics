# Plan The Full Dataset Fetch.

import requests

# Define API URL.
url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

# Define the parameters for the request.
params = {"$select": "count(*)"}

# Send the request.
response = requests.get(url, params=params)
response.raise_for_status()

print("Status code:", response.status_code)
print("Final URL:", response.url)

# Convert response to JSON
data = response.json()

print("Total number of rows available:", data[0]['count'])