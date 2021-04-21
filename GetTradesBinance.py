from binance.client import Client
import json
import time
from pybithumb.core import *
from pandas import DataFrame
import pandas as pd
import datetime
import math
from Bithumb import Bithumb
from BinanceApi import get_price
from CoinbitApi import get_price_Coinbit
from UpbitApi import get_price_Upbit

api_key="CPPjlXuX6pdrThteZi6z4bValjPEK4boN1HD1CfEOqySn0xxVaRbh51ZbzpiZ4OD"
api_secret="DTO53SRs53U9qO3FJX237zi56soKdE8uFbNz39Ew2Qcm0Zb55Gezl29XskBoHe1X"



import urllib.request, json 

client = Client(api_key, api_secret)

# get all symbol prices
prices = client.get_all_tickers()



#script Bithump


bit= Bithumb()
resp=bit.get_tickers()

price=bit.get_current_price("ALL")

list_dicts1 = []
dict_tmp = {}
for i in resp:
    dict_tmp["symbol"]=i
    dict_tmp["price"]=price[i]['closing_price']
    tiker=i+"USDT"
    data=get_price(tiker)
    dict_tmp["price2"]=data['price']
    pret3=get_price_Coinbit(i)
    dict_tmp["price3"]=int(float(pret3))
    tiker2="KRW-"+i
    pret4=get_price_Upbit(tiker2)
    dict_tmp["price4"]=pret4
    list_dicts1.append( dict_tmp )
    dict_tmp = {}




with open('pretBinance.json', 'w') as json_file:
    json.dump(list_dicts1, json_file)
