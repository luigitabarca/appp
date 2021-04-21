

import  json 
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError



def get_price(tiker):
    API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol='
    data={}
    req = Request(API_URL+tiker)
    try:
        url = urlopen(req)
    except HTTPError as e:
        data['symbol']=tiker
        data['price']=0
        return data
    except URLError as e:
        data['symbol']=tiker
        data['price']=0
        return data
    else:
        data = json.loads(url.read().decode())
        return data


