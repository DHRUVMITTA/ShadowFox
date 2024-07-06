import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/s?k=apple+iphone&crid=1GL52P2GX6JZI&sprefix=apple+iphon%2Caps%2C286&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
spans=soup.select("span.a-size-medium.a-color-base.a-text-normal")
for span in spans:
    print(span.string)