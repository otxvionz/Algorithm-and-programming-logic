import requests
from bs4 import BeautifulSoup

anchieta = 'https://anchieta.br'
r = requests.get(anchieta)
html_anchieta = r.text

soup = BeautifulSoup(html_anchieta)
for elem in soup.findall('div', class_='elementos widget.countaiener'):
    print(elem.text)
    
