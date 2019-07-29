import json

with open('cs1.json') as f:
    data= json.load(f)
for link in data['links']:
    print(link['points'],link['capacity'])
