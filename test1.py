# Import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get(
    'https://www.lalitmauritius.org/en/dictionary.html?letter=a')

soup = BeautifulSoup(page.text, "html.parser")

# dict = soup.find('span', id="dictionarylist")

kreol = soup.find('span', {"class": "main"})

eng = soup.find('div', {"class": "desc"})

# results = main.text + desc.text

# main = [kreol.text for kreol in dict.find_all('span')]

# desc = [eng.text for eng in dict.find_all('div')]

# # results = [{main[index]:cell.text for index,
# #             cell in enumerate(eng.find_all("div"))} for eng in desc]

print(kreol.text, eng.text)
