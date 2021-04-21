import urllib.request, json 
with urllib.request.urlopen("https://api.coinbit.com/api/v1.0/trading_pairs/") as url:
    data = json.loads(url.read().decode())

"""
list_dicts = []
dict_tmp = {}
for i in data:
    dict_tmp["symbol"]=i['base_symbol']
    dict_tmp["price"]=i['close_price']
    list_dicts.append( dict_tmp )
    dict_tmp = {}

with open('pretCoinbit.json', 'w') as json_file:
    json.dump(list_dicts, json_file)
"""

def get_price_Coinbit(tiker):
    for i in data:
        if tiker==i['base_symbol']:
            return i['close_price']
    return 0


