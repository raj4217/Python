import xml.etree.ElementTree as et
import requests


# src = requests.get("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=xml")
# with open('finance.xml', 'w') as f:
#     f.write(src.text)

tree = et.parse('finance.xml')
root = tree.getroot()

print(root.getchildren()[1])
currencies = []
price = []
for item in root.getchildren()[1]:
    for t in item.getchildren():
        # print(t.attrib)l
        if t.attrib['name'] == 'name':
            currencies.append(t.text)
        if t.attrib['name'] == 'price':
            price.append(t.text)

sum = 0
for i in list(zip(currencies, price)):
    if '/' not in i[0]:
        print(i)
        # sum += 1
# print(len(price), sum``)

import csv

with open('financial.csv','r',newline='') as wfile:

