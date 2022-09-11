from bs4 import BeautifulSoup
import requests

cr7_url = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page = requests.get(cr7_url)

soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

# die Tabelle mit den gewünschten Daten
table = soup.find('table',{'class':'infobox toccolours float-right toptextcells'})
# print(table)

data = table.findAll('tr')
print(data)

