import json
from pprint import pprint

import requests

# National Highway Traffic Safety Administration: NHTSA
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data':'5UX33DT07N9M86282'}
r = requests.post(url, data=post_fields)
# print(r.text)
# print(r.json()['Results'])
x = json.dumps(r.json(), indent=1)
# pprint(r.json()['Results'])
# pprint(r.json()['Results'][0])
print(len(r.json()['Results'][0]))
for item in r.json()['Results'][0]:
    # print(item, r.json()['Results'][0][item])
    # print(type(item))
    # print(f'/n')
    # pprint(item)
    pass
score = {item: r.json()['Results'][0][item] for item in r.json()['Results'][0] if r.json()['Results'][0][item] != ''}
pprint(score)
print(len(score))
# print(x)


