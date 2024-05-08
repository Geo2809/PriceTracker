import requests
from bs4 import BeautifulSoup
import lxml
from decimal import Decimal

def get_link_data(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'ro'
    }


    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    name = soup.find('h1', class_='page-title').text.strip()
    price = soup.find('p', class_='product-new-price').text.strip()[:-7]
    price = Decimal(price)
    return name, price


