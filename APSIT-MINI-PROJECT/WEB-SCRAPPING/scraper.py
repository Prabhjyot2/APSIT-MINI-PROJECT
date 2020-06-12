import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Honeywell-HAC25M1201W-53-Watt-Air-Purifier/dp/B0753HZPVS/ref=sr_1_fkmr1_1'
headers = {
    "USER AGENT":'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}

price = ""          # price has to declared out function then make it global in the function
title = ""         # title
def check_price():
    global price
    global title
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    try:
        title = soup.find(id="productTitle").get_text()
    except AttributeError:
        print("Product Title")

    try:
        price = soup.find(id="priceblock_ourprice").get_text()
    except AttributeError:
        print("Priceblock Ourprice")
       
    print(price)
    print(title.strip())
check_price()
