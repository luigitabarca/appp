import json
import logging
from urllib.parse import urlencode
from datetime import datetime, timedelta

import requests
import jwt



    #################
    # QUOTATION API #
    #################
def _get(url, **kwargs):
          
    resp = requests.get(url, **kwargs)
    if resp.status_code not in [200, 201]:
        logging.error('get(%s) failed(%d)' % (url, resp.status_code))
        if resp.text is not None:
            logging.error('resp: %s' % resp.text)
            raise Exception('request.get() failed(%s)' % resp.text)
        raise Exception(
            'request.get() failed(status_code:%d)' % resp.status_code)
    return json.loads(resp.text)





def get_market_all():
        
    url = 'https://api.upbit.com/v1/market/all'
    markets=[]
    market_all=_get(url)
    for i in market_all:
        if "KRW-" in i['market']:
            markets.append(i['market'])


    return markets

    
    
def get_ticker(markets):  
    url = 'https://api.upbit.com/v1/ticker'
    if not isinstance(markets, list):
        logging.error('invalid parameter: markets should be list')
        raise Exception('invalid parameter: markets should be list')

    if len(markets) == 0:
        logging.error('invalid parameter: no markets')
        raise Exception('invalid parameter: no markets')

    valid_market = []
    for market in markets:
        if market not in markets:
            logging.error('invalid market: %s' % market)
            raise Exception('invalid market: %s' % market)
        else:
            valid_market.append(market)

    markets_data = ','.join(valid_market)
    params = {'markets': markets_data}
    return _get(url, params=params)
    


allcurency=get_market_all()

#print(allcurency)


#print(m)
status=get_ticker(allcurency)

#print(status)
#for i in status:
   # print(i['market'] + '   ' + str(i['trade_price']))

"""
list_dicts = []
dict_tmp = {}
for i in status:
    dict_tmp["symbol"]=i['market']
    dict_tmp["pret"]=i['trade_price']
    list_dicts.append( dict_tmp )
    dict_tmp = {}

with open('pretUpbit.json', 'w') as json_file:
    json.dump(list_dicts, json_file)
   """ 

def get_price_Upbit(tiker):
    for i in status:
        if tiker==i['market']:
            return i['trade_price']
    return 0


p=get_price_Upbit("KRW-BTC")
print(p)