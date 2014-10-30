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
      index = line.find('{')
      if index == -1:
        continue
      source = line[:index - 1]
      if not gr.has_node(source):
        gr.add_node(source)
      start = text.index('::') + 1
      target_list = text[start:]
      # an empty list to store the final target senses
      targets = []

      if len(target_list) != 0:
        # using a stack structure to trim out our targets
        sense = ''
        while target_list:
          if '(' in target_list[0]:
            if sense != '':
              targets.append(sense)
              sense = ''
            target_list.pop(0)
            while len(target_list) != 0 and not ')' in target_list[0]:
              target_list.pop(0)
              if len(target_list) == 1:
                break
            if len(target_list) != 0:
              target_list.pop(0)
          elif '{' in target_list[0]:
            if sense != '':
              targets.append(sense)
              sense = ''
            target_list.pop(0)
            while len(target_list) != 0 and not '}' in target_list[0]:
              target_list.pop(0)
            if len(target_list) != 0:
              target_list.pop(0)

          elif '[' in target_list[0]:
            if sense != '':
              targets.append(sense)
              sense = ''
            target_list.pop(0)
            while len(target_list) != 0 and not ']' in target_list[0]:
              target_list.pop(0)
              if len(target_list) == 1:
                break
            if len(target_list) != 0:
              target_list.pop(0)
          else:
            sense += target_list.pop(0)
            if ',' in sense or ';' in sense:
              sense = sense[:-1]
              if sense != '':
                targets.append(sense)
                sense = ''
            else:
              sense += ' '

        # add the last sense in the translation stack 
        if sense != '':
          targets.append(sense)

      # trim out the trailing ' ' in the target strings
      # and add en edge for each sense if not already in the graph
      if len(targets) != 0:
        for target in targets:
          if target[-1] == ' ':
            index = targets.index(target)
            target = target[:-1]
            targets[index] = target
            if not gr.has_node(target):
              gr.add_node(target)
            if not gr.has_edge((source, target)):
              gr.add_edge((source, target))
          else:
            if not gr.has_node(target):
              gr.add_node(target)
            if not gr.has_edge((source, target)):
              gr.add_edge((source, target))
            
                  


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
#  print graph
  print
  # build the graph based on the french-en dict file
  graph = build_graph(file2, graph)
  
  print graph
  # keep building the graph based on the french-en dict file
 # graph = build_graph(file2, graph) 
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
