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
import re
import collections
from collections import defaultdict
import pythainlp
from itertools import chain
import scipy.sparse as sp
import string
from pythainlp.corpus import thai_stopwords
import time
# from attacut import tokenize, Tokenizer




def remove_space_re(content):
    sentences=[]
    for xs in content:
        # sentence = re.sub(r'[()"/”“.\xa0"‘’+-_%:;!]', "", xs, flags=re.UNICODE)
        # sentence = re.sub("'", r"", sentence, flags=re.UNICODE)
        sentence = re.sub(r"\s+", "", xs, flags=re.UNICODE)
        # sentence = re.sub("'", r"",sentence, flags=re.UNICODE)
        sentence = re.sub('‘’“”…', '', sentence)
        sentence = re.sub('\[.*?\]()', '', sentence)
        sentence = re.sub('[%s]' % re.escape(string.punctuation), '', sentence)
        sentence = re.sub('\d', '', sentence)
        sentence = re.sub('[A-Za-z]', '', sentence)
        sentence = re.sub('ฯ', '', sentence)
        sentence = re.sub('ๆ', '', sentence)
        sentence = re.sub('฿', '', sentence)
        sentence = re.sub('-', '', sentence)
        sentence = re.sub('\\u200b', '', sentence)
        sentence = re.sub('\xe0', '', sentence)
        # print(sentence)
        sentences.append(sentence)
    return remove_space(sentences)

def twolist_to_list(lis):
    b = []
    for xs in lis:
        for x in xs:
            b.append(x)
    return b
def tuple_merge(g1) :
    #   https://stackoverflow.com/questions/52454582/merge-tuples-with-the-same-key
    g2=twolist_to_list(g1)
    # print(g2)
    # print('g2:',g2)
    c = collections.defaultdict(list)
    for a,b in g2:
        # if b is None:
        #     b=' '
        c[a].extend(b)  # add to existing list or create a new one
        
    return list(c.items())

def get_sentence(detail):
    t = []
    for tag in detail:
        t.append(tag.text.strip())
        # p = tag.find("div")
        # y = tag.findAll("sub")
        # print(t)
    return t
# https://thispointer.com/python-how-to-remove-duplicates-from-a-list/
'''
    Remove duplicate elements from list
'''
def removeDuplicates(listofElements):

    # Create an empty list to store unique elements
    uniqueList = []

    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        # print(elem)
        if elem not in uniqueList:
            uniqueList.append(elem)

    # Return the list of unique elements
    return uniqueList

def split_word(sentence):
    w = []
    for i, l in enumerate(sentence):
        if i > 3:
            y = sentence[i].split("\n")
            # print(y[2].strip())
            p = word_tokenize(y[2], engine="newmm")
            # print(p)
            w.append(p)
    list_word = [x for xs in w for x in xs]
    return list_word
def word_tokenize_al(sentence):
    w = []
    for i in sentence:
        p = word_tokenize(i, engine="newmm")
        w.append(p)
    return twolist_to_list(w)
def returnspace(sen):
    if sen is  None:
        sen=[]
    else:
        sen=sen
    return sen
def remove_space(word1):
    py = []
    for u in word1:
        if u == '':
            # print(u)
            pass
        else:
            py.append(u)
    return py

def frequency_word(list_word):
    fdist1 = nltk.FreqDist(list_word)
    # print (fdist1.most_common(100))
    z = fdist1.most_common(25)
    df = pd.DataFrame(list(z), columns=["Word", "count"])
    # print(df)

    return df


#pythai
def frequency_word_pythai(list_word,i):
    d = rank(list_word)
    # print (fdist1.most_common(100))
    # z=fdist1.most_common(25)
    df = pd.DataFrame(list(d.items()), columns=["Word", "count"])
    # df.to_csv(f'{i+1}.csv')
    print(df)
    return df

def combine_dict(p,q,r, s,u,v,w):
    dd = defaultdict(list)
    for d in (p,q,r, s,u,v,w): # you can list as many input dicts as you want here
        for key, value in d.items():
            for c in value :
                # print('c:',c)
                # print('value',value)
                dd[key].append(c)
    return dd


def tokenize_text_list(ls):
    start = time.process_time()
    print("working on")
    g = list(
        chain.from_iterable([
            pythainlp.tokenize.word_tokenize(l, engine='newmm') for l in ls
        ]))
    # print(g)
    print(time.process_time() - start)
    return g




def text_to_bow(tokenized_text, vocabulary_, method):
    """ฟังก์ชันเพื่อแปลงลิสต์ของ tokenized text เป็น sparse matrix"""
    n_doc = len(tokenized_text)
    values, row_indices, col_indices = [], [], []
    k={}
    for r, tokens in enumerate(tokenized_text):
        # print('r:', r)
        # print(r,frequency_word(tokens))
        # print('tokens:', tokens)
        feature = {}
        for token in tokens:
            word_index = vocabulary_.get(token)
            # k[word_index]=token
            if word_index is not None:
                if word_index not in feature.keys():
                    feature[word_index] = 1
                else:
                    feature[word_index] += 1
        
        for c, v in feature.items():
            values.append(v)
            row_indices.append(r)
            col_indices.append(c)

    # document-term matrix in sparse CSR format
    X = sp.csr_matrix((values, (row_indices, col_indices)),
                      shape=(n_doc, len(vocabulary_)))
    return X
def text_to_bow_stopword(tokenized_text, vocabulary_):
    """ฟังก์ชันเพื่อแปลงลิสต์ของ tokenized text เป็น sparse matrix"""
    n_doc = len(tokenized_text)
    values, row_indices, col_indices = [], [], []
    stop_words = set(thai_stopwords()) 
    for r, tokens in enumerate(tokenized_text):
        # print('r:', r)
        # print('tokens:', tokens)
        filtered_sentence = [w for w in tokens if not w in stop_words]
        # print(r,frequency_word(filtered_sentence))
        # print('filtered_sentence',filtered_sentence)
        feature = {}
        for token in filtered_sentence:
            word_index = vocabulary_.get(token)
            if word_index is not None:
                if word_index not in feature.keys():
                    feature[word_index] = 1
                else:
                    feature[word_index] += 1
        # print('r:',r)
        # print('feature:',feature)
        for c, v in feature.items():
            values.append(v)
            row_indices.append(r)
            col_indices.append(c)

    # document-term matrix in sparse CSR format
    X = sp.csr_matrix((values, (row_indices, col_indices)),
                      shape=(n_doc, len(vocabulary_)))
    return X

