#! /usr/bin/env python

from __future__ import division

import os

import nltk, re, pprint
from nltk import *
from nltk.corpus import brown
import urllib 
#from urllib import request

import bs4
from bs4 import BeautifulSoup # get text out of HTML

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
response = urllib.urlopen(url)
html = response.read().decode('utf8')
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
#print(tokens)
text = nltk.Text(tokens)
print(text)
words = [w.lower() for w in tokens]
vocab = sorted(set(words))
#print(vocab)
print(re.split(' ', raw))

#for word in tokens:
#    freqdist[word.lower()] += 1
#    print(freqdist.most_common(n))

tree1 = nltk.Tree('NP', ['Alice'])
print(tree1)
