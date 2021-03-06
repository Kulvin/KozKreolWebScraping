# Import libraries
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://www.lalitmauritius.org/en/dictionary.html?letter=a')

soup = BeautifulSoup(page.content, 'html.parser')

dict = {}
rows = soup.find_all('li')

for row in rows:
    try:
        kreol = row.find('span', {'class': 'main'})
        eng = row.find('div', {'class': 'desc'})
        dict[kreol.text] = {eng.text}
    except AttributeError:
        pass

print(dict)
