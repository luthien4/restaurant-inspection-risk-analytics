# Download the full dataset in multiple JSON chunk files.

import json
from pathlib import Path

import requests


url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

params = {
    "$select": "count(*)"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

num_rows = int(data[0]['count'])

chunk_size = 50000
i = 1
offsets = []
for offset in range(0, num_rows, chunk_size):

    offsets.append(offset)
    params_current = {'$limit': chunk_size,
                      '$offset': offset,
                      '$order': 'inspection_id'
                     }
    chunk_end = min(offset + chunk_size, num_rows)

    response = requests.get(url, params=params_current)
    response.raise_for_status()

    data_offset = response.json()

    output_path = Path(f"data/raw/food_inspections_chunk_{offset:06d}.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data_offset, file, indent=2)

    print("Chunk number:", i)
    print("offset:", offset)
    print("Rows:", [offset, chunk_end])
    print("Records downloaded:", len(data_offset))
    print("Output path:", output_path)

    i += 1

print("Offsets downloaded:", offsets)
print("Total chunks downloaded:", len(offsets))