# Stage 2/6: Correct syntax

import json
import re

data = json.loads(input())
errors = {
    'stop_name': sum(not re.match(r'^[A-Z].+ (Road|Avenue|Boulevard|Street)$', entry['stop_name']) for entry in data),
    'stop_type': sum(entry['stop_type'] not in ('S', 'F', 'O', '') for entry in data),
    'a_time': sum(not re.match(r'^([01]\d|2[0-3]):[0-5]\d$', entry['a_time']) for entry in data)
}
print(f'Format validation: {sum(errors.values())} errors')
print('\n'.join([f'{key}: {value}' for key, value in errors.items()]))