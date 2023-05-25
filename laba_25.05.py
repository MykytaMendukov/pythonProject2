import requests
from bs4 import BeautifulSoup
class NotPageFound(Exception):
    def __init__(self):
        self.response.status_code = None
#1
response = requests.get("https://exampdawdle.com")
n = NotPageFound(Exception)
n.response = response.status_code
try:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title').text
    print(title)
except NotPageFound as e:
    print(f'No connection {e}')

#2

response = requests.get("https://uk.wikipedia.org/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.find_all('img')
    for i in img:
        print('https://' + i['src'])

#3

response = requests.get("https://www.example.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    soup_list = soup.find_all("a")
    for link in soup_list:
        href = link.get("href")
        print(href)

#4

response = requests.get("https://www.example.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script in soup.find_all(['style', 'script']):
        script.extract()
    text = ' '.join(soup.stripped_strings)
    words = len(text.split())
    print(words)
