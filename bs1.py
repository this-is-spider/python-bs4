from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html, 'lxml')
text = soup.find_all(id='text')
print(text[0].get_text())
# items = soup.findAll('span', {"class": "red"})
# for item in items:
#     print(item.get_text())
# print(soup.findAll(id='text', recursive=False))