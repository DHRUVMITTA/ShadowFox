import requests
from bs4 import BeautifulSoup
with open("demo.html","r") as f:
    html_doc=f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)
print(soup.div)
print(soup.find_all('div'))
for link in soup.find_all('a'):
    print(link.get('href'))
