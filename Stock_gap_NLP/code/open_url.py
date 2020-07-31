from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pythainlp.tokenize import word_tokenize
import csv
import nltk
import matplotlib.pyplot as plt
import datetime
from pythainlp.util import rank



def openhtml(my_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=my_url, headers=headers)
    uClient = urlopen(req)
    page_html = uClient.read()
    uClient.close()
    soup = BeautifulSoup(page_html, "html.parser")
    return soup

