from bs4 import BeautifulSoup
import bs4
import requests


cr7_url: str = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page: requests.Response = requests.get(cr7_url)

soup: bs4.BeautifulSoup = BeautifulSoup(page.text, "html.parser")
soup.prettify()


# die Tabelle mit den gewünschten Daten
table: bs4.element.Tag = soup.find('table',{'class':'infobox toccolours float-right toptextcells'})

data_td_tags: bs4.element.ResultSet = table.findAll('td')

# dictionary, um die Daten zur Person zu speichern
person: dict = {}


for data in data_td_tags:
    if data.text.find("Geburtstag") == 0:
        # sucht das gewünschte Element heraus
        element: bs4.element.Tag = soup.find(text="Geburtstag").findNext('td').contents[0]
        #print(a.next_element)
        person.update({"Geburtstag":element.next_element})

print(person)













