from bs4 import BeautifulSoup
import requests

cr7_url = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page = requests.get(cr7_url)

soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

# die Tabelle mit den gewünschten Daten
table = soup.find('table',{'class':'infobox toccolours float-right toptextcells'})
# print(table)

data = table.findAll('td')

# Ganzen Attribute sind in <b>´s -> diese durchsuchen mit immer next und dann extern einfach den Tag nach diesem
# als value einfügen

[print(type(element.b)) for element in data]

#last_a_tag = soup.find("b")
#print(last_a_tag.next_element)

#data_key = table.findAll('b')
#print(data_key)


