# Stage 4/6: Special stops

import json

data = json.loads(input())

for bus_id in set(rec['bus_id'] for rec in data):
    if sum(rec['stop_type'] == 'S' for rec in data if rec['bus_id'] == bus_id) != 1\
            or sum(rec['stop_type'] == 'F' for rec in data if rec['bus_id'] == bus_id) != 1:
        print(f'There is no start or end stop for the line: {bus_id}')
        exit(0)

starts = set(rec['stop_name'] for rec in data if rec['stop_type'] == 'S')
print(f'Start stops: {len(starts)} {sorted(list(starts))}')

tranfers = set(trans['stop_name'] for trans in data if sum(rec['stop_name'] == trans['stop_name'] for rec in data) > 1)
print(f'Transfer stops: {len(tranfers)} {sorted(list(tranfers))}')

finishes = set(rec['stop_name'] for rec in data if rec['stop_type'] == 'F')
print(f'Finish stops: {len(finishes)} {sorted(list(finishes))}')