from bs4 import BeautifulSoup
import requests

cr7_url = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page = requests.get(cr7_url)

print(page.content)


soup = BeautifulSoup(page.content, "html.parser")
print (soup)