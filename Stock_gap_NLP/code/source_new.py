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
from  open_url import *
from  process_wording import *


def bangkokbiznews(url_new):
    try:
        soup = openhtml(url_new)
        containers_1 = soup.findAll("h1")
        head1_1=get_sentence(containers_1)
        head1=remove_space_re(head1_1)
        # print( x[0])
        containers = soup.findAll("h2")
        head2_1=get_sentence(containers)
        head2=remove_space_re([head2_1[0]])
        # print( x[0])
        containers_2 = soup.findAll("p")
        content_1=get_sentence(containers_2)
        if len(content_1) >9 :
            content=remove_space_re(content_1[0:-9])
        else:
            content=remove_space_re(content_1[0:-1])
            # print( x[0:-9])
        t= twolist_to_list([head1,head2,content])
        # return   t
    except:
        t=[]
    return   t
def hooninside(url_new):
    try:
        soup = openhtml(url_new)
        containers = soup.findAll("h1")
        x = get_sentence(containers)
        p=remove_space_re([x[2]])
        # print(x[2])
        containers_1 = soup.findAll("div", {"class": "detail-block"})
        con=[]
        for tag in containers_1:
            y = tag.findAll("p")
            y = get_sentence(y)
            p=remove_space_re(y)
            con.append(p)
        b = twolist_to_list(con)
            # print(y)
            # print(len(y))
        t=  twolist_to_list([p,b])
    except:
         t=[]
    return   t
    

def hoonsmart(url_new):
    try:
        soup = openhtml(url_new)
        containers = soup.findAll("h1")
        x = get_sentence(containers)
        p_1=remove_space_re(x)
        # print(x)
        containers_1 = soup.findAll("div", {"class": "entry-content"})
        con=[]
        for tag in containers_1:
            y = tag.findAll("p")
            y = get_sentence(y)
            # print(y)
            p=remove_space_re(y)
            con.append(p)
        b = twolist_to_list(con)
        t= twolist_to_list([p_1,b])
    except:
        t=[]
    return   t

def innnews(url_new):
    try:
        soup = openhtml(url_new)
        # print(soup)
        containers = soup.findAll("h1")
        x=get_sentence(containers)
        p_1=remove_space_re(x)
        # print( x)
        containers = soup.findAll("h2")
        x=get_sentence(containers)
        p_2=remove_space_re(x)
        # print( x)
        containers_1 = soup.findAll("div", {"class": "entry-content entry clearfix"})
        con=[]
        for tag in containers_1:
            y = tag.findAll("p")
            y = get_sentence(y)
            
            p=remove_space_re(y)
            con.append(p)
        b = twolist_to_list(con)
        t= twolist_to_list([p_1,p_2,b])
    except:
        t=[]
    return   t


def mgronline(url_new):
    try:
        soup = openhtml(url_new)
        containers = soup.findAll("h1")
        x = get_sentence(containers)
        print(x)
        containers_1 = soup.findAll("div", {"class": "article-content"})
        print(containers_1[0].div.text.strip())
    except:
            pass
        
def posttoday(url_new):
    try:
        soup = openhtml(url_new)
        containers = soup.findAll("h1")
        x = get_sentence(containers)
        p_1=remove_space_re([x[1]])
        # print(p_1)
        containers_1 = soup.findAll("div", {"class": "articleContents2"})
        con=[]
        for tag in containers_1:
            y = tag.findAll("p")
            y = get_sentence(y)
            p=remove_space_re(y)
            con.append(p)
        b = twolist_to_list(con)
        # print(b)
        t= twolist_to_list([p_1,b])
    except:
        t=[]
    return   t

def thunhoon(url_new):
    try:
        soup = openhtml(url_new)
        containers = soup.findAll("h2")
        x = get_sentence(containers)
        p_1=remove_space_re([x[0]])
        # print(x[0])
        containers_1 = soup.findAll("div", {"class": "entry-content"})
        con=[]
        for tag in containers_1:
            y = tag.findAll("p")
            y = get_sentence(y)
            p=remove_space_re(y)
            con.append(p)
        t= twolist_to_list(con)
        
    except:
        t=[]
    return   t
def kaohoon(url_new):
    try:
        soup = openhtml(url_new)
        containers = soup.findAll("h1")
        x = get_sentence(containers)
        p_1=remove_space_re([x[0]])
        # print(x[0])
        containers_1 = soup.findAll("div", {"class": "content-main entry-content"})
        con=[]
        for tag in containers_1:
            y = tag.findAll("p")
            y = get_sentence(y)
            p=remove_space_re(y)
            con.append(p)
        t= twolist_to_list(con)
        
    except:
        t=[]
    return   t
def efinancethai(url_new):
    soup = openhtml(url_new)
    containers = soup.findAll("h1")
    x = get_sentence(containers)
    # print(x)
    print(x[2])
    containers_1 = soup.findAll("div", {"class": "col-lg-12 col-md-12"})
    for i,tag in enumerate(containers_1):
        y = tag.findAll("p")
        y = get_sentence(y)
        print(y)
        print(len(y))
        z= tag.findAll("span")
        z = get_sentence(z)
        print("span:",z)
        # print(len(z))
        z= tag.findAll("br")
        z = get_sentence(z)
        print("br:",z)
        print(len(z))
        # z= tag.findAll("strong")
        # z = get_sentence(z)
        # print("strong:",z)
        # print(len(z))