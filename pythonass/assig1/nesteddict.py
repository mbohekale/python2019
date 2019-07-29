import json
with open("cs1.json", 'r') as f:
    mydict = json.load(f)
    for mydict_data in mydict['simulation']['demands']:
        print(mydict_data)
    print(type(mydict['simulation']['demands']))         
