# Calculate the list of offsets needed to download all rows in chunks.

import requests

url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

# Define the parameters for the request.
params = {"$select": "count(*)"
          }

response = requests.get(url, params=params)
response.raise_for_status()

# Checking the status code for the request.
print("Status code:", response.status_code)

data = response.json()

# Convert the total of rows into an integer.
num_rows = int(data[0]['count'])

# Compute the number of chunks
chunk_size = 50000
i = 1
offsets = []
for chunk in range(0, num_rows, chunk_size):
    offsets.append([chunk, min(chunk + chunk_size, num_rows)])
    print(f"Chunk {i}: [{chunk}, {min(chunk + chunk_size, num_rows)}]")
    i += 1

print("Total rows:", num_rows)
print("Chunk size:", chunk_size)
print("Number of chunks:", len(offsets))
print("Offsets:", offsets)


