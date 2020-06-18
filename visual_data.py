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

def line_graph_frquency(x, y, stock,date):
    plt.rcParams['font.family'] = 'Tahoma'
    # plt.rcParams['font.size']=20 # font size
    plt.plot(x, y, color='b')
    plt.xticks(x, rotation='vertical')
    plt.savefig(f'{stock}_{date}.png')
    # plt.show()
    plt.cla()

