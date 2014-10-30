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
import codecs
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




def build_graph(filename, graph):
  """
  Given the dictionary file, build the graph for the dictionary
  return the graph built
  """
  gr = graph 

  # open and read the file
  f = codecs.open(filename, 'rU', 'utf-8')
  
  # outf = codecs.open('sample_graph.txt', 'w', 'utf-8')
  # loop through every single line in the dictionary and parse
  # for translation information
  source = ''
  for line in f:
    text = line.split()
    if len(text) != 0:

      source = " ".join(text[:text.index('{')])
      start = text.index('::') + 1
      target_list = text[start:]
      # an empty list to store the final target senses
      targets = []
      prev = 0
      current = 0
      curly = 0
      if len(target_list) != 0:
        # using a stack structure to trim out our targets
        while target_list:
          if '(' in target_list[0]:
            while not ')' in target_list[0]:
              target_list.pop(0)
            target_list.pop(0)
          elif '{' in target_list[0]:
            target_list.pop(0)


"""
        for target in target_list:
          if '{' in target:
            curly = target_list.index(target)

          if ';' in target or ',' in target:
            current = target_list.index(target)
            if current == 0:
              targets.append(target[:-1])
            else:
              if prev < curly and curly < current:
"""                
        if not gr.has_node(source):
          gr.add_node(source)

  # outf.close()
  f.close()

  return gr 

def main():
  """ the main function to execute the CQC algorithm """

  args = sys.argv[1:]

  if not args:
    print 'usage: dict1 dict2'
    sys.exit(1)
  
  file1 = args[0]
  file2 = args[1]

  # Initialize a empty graph G = (V, E)
  graph = digraph()
  
  # build the graph based on the en-french dict file
  graph = build_graph(file1, graph)
  
  print graph
  # keep building the graph based on the french-en dict file
 # graph = build_graph(file2, graph) 
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
