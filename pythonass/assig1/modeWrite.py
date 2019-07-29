#delete the capacity
import json

with open('cs1.json') as f:
    data= json.load(f)
for link in data['links']:
    del link['capacity']
with open('new_links.json', "w") as f:
    json.dump(data, f,indent=2)
    print(data)
