
from pybithumb.core import *
from pandas import DataFrame
import pandas as pd
import datetime
import math

class Bithumb:
    

    @staticmethod
    def _convert_unit(unit):
        try:
            unit = math.floor(unit * 10000) / 10000
            return unit
        except:
            return 0

    @staticmethod
    def get_tickers(payment_currency="KRW"):
        """
        빗썸이 지원하는 암호화폐의 리스트
        :param payment_currency : KRW
        :return:
        """
        resp = None
        try:
            resp = PublicApi.ticker("ALL", payment_currency)
            data = resp['data']
            tickers = [k for k, v in data.items() if isinstance(v, dict)]
            return tickers
        except Exception:
            return resp

    
    @staticmethod
    def get_current_price(order_currency, payment_currency="KRW"):
        """
        최종 체결 가격 조회
        :param order_currency   : BTC/ETH/DASH/LTC/ETC/XRP/BCH/XMR/ZEC/QTUM/BTG/EOS/ICX/VEN/TRX/ELF/MITH/MCO/OMG/KNC
        :param payment_currency : KRW
        :return                 : price
        """
        resp = None
        try:
            resp = PublicApi.ticker(order_currency, payment_currency)
            if order_currency != "ALL":
                return float(resp['data']['closing_price'])
            else:
                del resp["data"]['date']
                return resp["data"]
                
        except Exception:
            return resp


