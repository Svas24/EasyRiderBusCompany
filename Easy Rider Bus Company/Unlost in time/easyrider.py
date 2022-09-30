# Stage 5/6: Unlost in time

import json

stops = json.loads(input())
print('Arrival time test:')
errors = False
for bus_id in set(stop['bus_id'] for stop in stops):
    last = next(filter(lambda stop: stop['bus_id'] == bus_id and stop['stop_type'] == 'S', stops))
    while last['next_stop'] != 0:
        current = next(filter(lambda stop: stop['bus_id'] == bus_id and stop['stop_id'] == last['next_stop'], stops))
        if current['a_time'] <= last['a_time']:
            print(f"bus_id line {bus_id}: wrong time on station {current['stop_name']}")
            errors = True
            break
        last = current
if not errors:
    print("OK")