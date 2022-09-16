from bs4 import BeautifulSoup
import bs4
import requests


cr7_url: str = "https://de.wikipedia.org/wiki/Cristiano_Ronaldo"
page: requests.Response = requests.get(cr7_url)

soup: bs4.BeautifulSoup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())