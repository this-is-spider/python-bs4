from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html)
# for child in soup.find("table", {"id": "giftList"}).children:
#     print(child)
for sibling in soup.find("table", {"id": "giftList"}).next_siblings:
    print(sibling)