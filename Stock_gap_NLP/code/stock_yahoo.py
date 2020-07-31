import os
import pandas as pd
import numpy as np
from yahoofinance import HistoricalPrices

def download_historicaldata(tag,start, end):
    stocks =str(tag+'.BK.csv')
    stock= 'yahoo_finance\\'+stocks
    # print(stock)
    if os.path.exists(stock):
        print('Remove  ' + tag)
        os.remove(stock)
        print('Download  ' + tag)
        req = HistoricalPrices(tag+'.BK',start, end)
        req.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\yahoo_finance\\'+tag+'.BK.csv')
    else:
        print('Download  ' + tag)
        req = HistoricalPrices(tag+'.BK',start, end)
        req.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\yahoo_finance\\'+tag+'.BK.csv')
    # return  pd.read_csv(stock)
def status_stock(diff):
    if diff >0:
        x='positive'
    elif diff <0:
        x='negative'
    elif diff ==0:
        x='neutral'
    else:
        x='None'
    return x