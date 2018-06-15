import json
import pandas as pd
import requests

src = requests.get("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")

data = json.loads(src.text)

df = pd.DataFrame([x['resource']['fields'] for x in data['list']['resources']])

df.to_csv('json.csv', index=False)

with open('finance.json', 'w') as wf:
    json.dump(data, wf, indent=2)
