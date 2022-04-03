import requests
from bs4 import BeautifulSoup
import fake_useragent
import lxml

ua = fake_useragent.UserAgent()

headers = {
    "accept": "*/*",
    "user-agent": ua.random
    }

cookies = {
    "globus_hyper_id": "77",
    "globus_hyper_name": "%D0%A2%D1%83%D0%BB%D0%B0"
}

url = 'https://www.globus.ru/catalog/'

req = requests.get(url, headers=headers, cookies=cookies)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(req.text)
