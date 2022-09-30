# Stage 3/6: Bus line info

import json

data = json.loads(input())
print('Line names and number of stops:')
for bus_id in set(entry['bus_id'] for entry in data):
    print(f"bus_id: {bus_id}, stops: {sum(entry['bus_id'] == bus_id for entry in data)}")