#!/usr/bin/python -tt
# Copyright Albert Hongbo Yang 2014 

# CQC Algorithm for enriching and enhancing disambiguation of a bilingual
# dictiontary. English-French and French-English


from __future__ import division

import os

import nltk, re, pprint
from nltk import *
from nltk.corpus import brown
import urllib 
#from urllib import request

import bs4
from bs4 import BeautifulSoup # get text out of HTML

# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# response = urllib.urlopen(url)
# html = response.read().decode('utf8')
# raw = BeautifulSoup(html).get_text()
# tokens = word_tokenize(raw)
# print(tokens)
# text = nltk.Text(tokens)
# print(text)
# words = [w.lower() for w in tokens]
# vocab = sorted(set(words))
# print(vocab)
# print(re.split(' ', raw))

# for word in tokens:
#   freqdist[word.lower()] += 1
#   print(freqdist.most_common(n))

# tree1 = nltk.Tree('NP', ['Alice'])
# print(tree1)
import sys
sys.path.append('..')
#sys.path.append('/usr/lib/graphviz/python/')
sys.path.append('/usr/local/Cellar/graphviz/')
#import gv

#from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms.cycles import find_cycle
from pygraph.algorithms.critical import *

# created a directed graph
gr = digraph()

gr.add_nodes(["Portugal","Spain","France","Germany","Belgium","Netherlands","Italy"])
gr.add_nodes(["Switzerland","Austria","Denmark","Poland","Czech Republic","Slovakia","Hungary"])
gr.add_nodes(["England","Ireland","Scotland","Wales"])

gr.add_edge(("Portugal", "Spain"))
gr.add_edge(("Spain","France"))
gr.add_edge(("France","Belgium"))
gr.add_edge(("France","Germany"))
gr.add_edge(("France","Italy"))
gr.add_edge(("Belgium","Netherlands"))
gr.add_edge(("Germany","Belgium"))
gr.add_edge(("Germany","Netherlands"))
gr.add_edge(("England","Wales"))
gr.add_edge(("England","Scotland"))
gr.add_edge(("Scotland","Wales"))
gr.add_edge(("Switzerland","Austria"))
gr.add_edge(("Switzerland","Germany"))
gr.add_edge(("Switzerland","France"))
gr.add_edge(("Switzerland","Italy"))
gr.add_edge(("Austria","Germany"))
gr.add_edge(("Austria","Italy"))
gr.add_edge(("Austria","Czech Republic"))
gr.add_edge(("Austria","Slovakia"))
gr.add_edge(("Austria","Hungary"))
gr.add_edge(("Denmark","Germany"))
gr.add_edge(("Poland","Czech Republic"))
gr.add_edge(("Poland","Slovakia"))
gr.add_edge(("Poland","Germany"))
gr.add_edge(("Czech Republic","Slovakia"))
gr.add_edge(("Czech Republic","Germany"))
gr.add_edge(("Slovakia","Hungary"))
gr.add_edge(("Germany", "Austria"))
gr.add_edge(("Germany", "Portugal"))


if gr.has_edge(("Spain", "France")):
  print 'France is reachable from Spain'
st, pre, post = depth_first_search(gr, root='Germany')
print st
print pre

print (gr.neighbors("Germany"))
print
print (gr.incidents('Germany'))
