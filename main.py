from bs4 import BeautifulSoup
import bs4
import requests
from datetime import datetime


url: str = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page: requests.Response = requests.get(url)

soup: bs4.BeautifulSoup = BeautifulSoup(page.text, "html.parser")
soup.prettify()



# die Tabelle mit den gewünschten Daten
table: bs4.element.Tag = soup.find('table',{'class':'infobox toccolours float-right toptextcells'})

data_td_tags: bs4.element.ResultSet = table.findAll('td')

# dictionary, um die Daten zur Person zu speichern
person: dict = {}


for data in data_td_tags:
    if data.text.find("Voller Name") == 0:
        # sucht das gewünschte Element heraus
        element: bs4.element.Tag = soup.find(text="Voller Name").findNext('td').contents[0]
        name = str(element)
        name = name.replace("\n","")
        person.update({"Voller Name":name})

    if data.text.find("Geburtstag") == 0:
        # sucht das gewünschte Element heraus
        element: bs4.element.Tag = soup.find(text="Geburtstag").findNext('td').contents[0]
        person.update({"Geburtstag":element.next_element+" "+element.findNext('a').text})

    if data.text.find("Geburtsort") == 0:
        # sucht das gewünschte Element heraus
        element: bs4.element.Tag = soup.find(text="Geburtsort").findNext('td').contents[0]
        person.update({"Geburtsort":element.next_element+", "+ element.findNext('a').text})

    if data.text.find("Größe") == 0:
        # sucht das gewünschte Element heraus
        element: bs4.element.Tag = soup.find(text="Größe").findNext('td').contents[0]
        height_in_cm: float = float(element.replace(" cm",""))
        person.update({"Größe":height_in_cm})

    if data.text.find("Position") == 0:
        # sucht das gewünschte Element heraus
        element: bs4.element.Tag = soup.find(text="Position").findNext('td').contents[0]
        person.update({"Position":element.next_element+", "+ element.findNext('a').text})



#print(person)

for value in person.values():
    print(type(value))










