# Stage 6/6: On-demand

import json

stops = json.loads(input())
print('On demand stops test:')
wrongs = []
for o_stop_id in set(stop['stop_id'] for stop in stops if stop['stop_type'] == 'O'):
    if sum(stop['stop_id'] == o_stop_id for stop in stops) > 1:
        wrongs.append(next(filter(lambda stop: stop['stop_id'] == o_stop_id, stops))['stop_name'])
print(sorted(wrongs) if wrongs else 'OK')