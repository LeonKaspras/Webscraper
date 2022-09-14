Wichtig über HTML bzgl web scraping:
1. HTML besteht aus tags
    - diese werden von hypermarks -> "<>" umschlossen
2. Tags können Attribute haben
    - hypermarks + Attribut kommt vor und nach den Absatz, der dieses Attribut haben soll
    - Bsp: <strong> TEXT </strong> (würde den Text jetzt dick/bold machen)
3. Tags können in tags verwendet werden
    - Bsp:<strong> <em> TEXT </em> TEXT</strong> (für fett gedruckten Text, mit kursiv drinnen)

---------------------------------------------------------------------------------------------------------------------
Web scraping with Beatiful Soup in Python:

What is web scraping?
Extracting content and data from a website (the HTML code and with it, data stored in a database).
That makese it possible to replicate the entire content of a website elsewhere.

What is Beatiful Soup?
A Python library that is used for web scraping to pull the data out of HTML and XML files.
What Beatiful Soup is doing is, that it creates a parse tree from the source code of a page (extract data hierarchical)
to ensure better readability.

How does Web scraping work with BeatifulSoup in Python?
(knowledge taken from https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org)

<a> tag defines a hyperlink, which is used to link from one page to another.
<tr> tag defines a row in an HTML table. A <tr> element contains one or more <th> or <td> elements.

To benefit from the advantage of Beatiful Soup to ensure better readability you import the library,
store the html content in a variable, then give it the content and prettify that. 
In Code it looks like that:
from bs4 import BeautifulSoup
import requests

content = "WEBSITE URL"
page = requests.get(content)

soup = BeautifulSoup(page.text, "html.parser")
soup.prettify()

