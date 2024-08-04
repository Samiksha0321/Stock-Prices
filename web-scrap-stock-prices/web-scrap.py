import requests 
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \ Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \ Chrome/84.0.4147.105 Safari/537.36'}

urls = [
    'https://www.investing.com/equities/nike',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/mcdonalds',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney',
    ]

all = []
for url in urls:
    page = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        company = soup.find('h1', {'class': 'text-2xl font-semibold \ instrument-header_title__gCaMF \ mobile:mb-2'}).text # company name
        price = soup.find('div', {'class': 'nstrument-price_instrument-price__xfgbB flex items-end flex-wrap font-bold'}).find_all('span')[0].text # current stock price
        change = soup.find('div', {'class': 'nstrument-price_instrument-price__xfgbB flex items-end flex-wrap font-bold'}).find_all('span')[2].text # change in percentage of stocks
        volume = soup.find('div', {'class': 'trading-hours_value__5_NnB'}).text # volume of stocks
        
    except:
        print('Change Element id')