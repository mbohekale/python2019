import json
from urllib.request import urlopen
with urlopen("https://api.github.com/users/hadley/orgs/quote?format=json") as response:
             source = response.read()
             print(source)
