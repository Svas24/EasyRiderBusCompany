# Stage 1/6: Checking the data type

import json

data = json.loads(input())
errors = dict()
errors['bus_id'] = sum(type(entry['bus_id']) is not int for entry in data)
errors['stop_id'] = sum(type(entry['stop_id']) is not int for entry in data)
errors['stop_name'] = sum(type(entry['stop_name']) is not str or len(entry['stop_name']) < 1 for entry in data)
errors['next_stop'] = sum(type(entry['next_stop']) is not int for entry in data)
errors['stop_type'] = sum(entry['stop_type'] not in ('', 'S', 'F', 'O') for entry in data)
errors['a_time'] = sum(type(entry['a_time']) is not str or len(entry['a_time']) < 4 for entry in data)

print(f'Type and required field validation: {sum(errors.values())} errors')
for key, value in errors.items():
    print(f'{key}: {value}')