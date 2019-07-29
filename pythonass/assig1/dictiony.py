import json
with open("cs1.json", 'r') as f:
    mydict = json.load(f)
def get_demands():
    question_access = mydict['simulation']['demands']
    for question_data in question_access:
        replies_access = question_data['demand']
        for replies_data in replies_access:
            demands = replies_data['']
            print(demands)
get_demands()
