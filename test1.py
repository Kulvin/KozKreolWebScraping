# Import libraries
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://www.lalitmauritius.org/en/dictionary.html?letter=a')

soup = BeautifulSoup(page.content, "html.parser")

dict = soup.find_all('ul', id="dictionarylist")

print(dict)
