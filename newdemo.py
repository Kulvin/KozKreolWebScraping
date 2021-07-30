# import libraries
import requests
from bs4 import BeautifulSoup

inp = input("Enter letter")
web = requests.get(
    'https://www.lalitmauritius.org/en/dictionary.html?letter='+inp)

data = web.content

soup = BeautifulSoup(data, features="html.parser")

tag = soup.find_all(("div", "desc") + ("span", "main"))


a = 1

for i in tag:

    print(a, ".", i.text)
    a = a+1

# print(tag)
