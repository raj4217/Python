import json
import pandas as pd
import requests

src = requests.get("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")

data = json.loads(src.text)

with open('finance.json', 'w') as wf:
    json.dump(data, wf, indent=2)

rates = {}
for x in data['list']['resources']:
    try:
        if '/' in x['resource']['fields']['name']:
            name = x['resource']['fields']['name']
            price = x['resource']['fields']['price']
    except:
        pass
    rates[name] = price
