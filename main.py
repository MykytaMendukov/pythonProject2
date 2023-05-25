import urllib.request

opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())
print('difference')

import requests

response1 = requests.get("https://coinmarketcap.com")
print(response1.content)
