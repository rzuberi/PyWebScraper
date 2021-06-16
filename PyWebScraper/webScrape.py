import requests
from selenium import webdriver
from bs4 import BeautifulSoup as BSHTML
import json

url = 'http://localhost:3000/static/index.html'
response = requests.get(url)
soup = BSHTML(response.content, "html.parser")

allImgs = soup.findAll('img', {'class': 'image-elt ng-lazyloaded'})

print(allImgs)

for img in allImgs:
    print(img)
    print("\n")

data = {}
data["product"] = []

i = 0
for img in allImgs:
  data["product"].append({
    "id": i,
    "title": img["alt"],
    "link": "https://www.bouyguestelecom.fr" + img["src"]
    })
  i +=1

with open('products.json', 'w') as outfile:
    json.dump(data, outfile)
