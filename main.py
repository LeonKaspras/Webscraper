from bs4 import BeautifulSoup
import bs4
import requests

cr7_url: str = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page: requests.Response = requests.get(cr7_url)

soup: bs4.BeautifulSoup = BeautifulSoup(page.text, "html.parser")
soup.prettify()


# die Tabelle mit den gewünschten Daten
table: bs4.element.Tag = soup.find('table',{'class':'infobox toccolours float-right toptextcells'})

data: bs4.element.ResultSet = table.findAll('td')

# gibt alle Elemete von data aus
for data in data:
    print(type(data.text))













