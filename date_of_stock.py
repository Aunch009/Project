from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pythainlp.tokenize import word_tokenize
import csv
import nltk
import matplotlib.pyplot as plt
import datetime
from pythainlp.util import rank
from datetime import timedelta


def date_to_date():
    x = datetime.date.today()
    # print(x.strftime("%A"))
    return x

def date_month_2019(x,y):
    # print(x,y)
    month1=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i,v in enumerate(month1):
        # print(i+1,v)
        if v==y :
            # print(v,y,i+1)
            return datetime.date(2019,i+1,int(x))
def date_month_2020(x,y):
    # print(x,y)
    month1=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i,v in enumerate(month1):
        # print(i+1,v)
        if v==y :
            # print(v,y,i+1)
            return datetime.date(2020,i+1,int(x))
            
def dateform (x):
    z = x.split('/')
    return str(datetime.date(int(z[2]),int(z[1]),int(z[0])))


