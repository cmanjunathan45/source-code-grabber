import requests
from bs4 import BeautifulSoup
url=input("Enter the URL You Want To get Source Code : ")
page=requests.get(url)
parse=BeautifulSoup(page.content,'html.parser')
print(parse.prettify())