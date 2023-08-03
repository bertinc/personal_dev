import requests
from bs4 import BeautifulSoup
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())