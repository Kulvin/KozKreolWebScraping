# Import libraries
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://www.lalitmauritius.org/en/dictionary.html?letter=a')

soup = BeautifulSoup(page.content, "html.parser")

dict = soup.find('ul', id="dictionarylist")

headers = [heading.text for heading in dict.find_all('li')]

print(headers)
