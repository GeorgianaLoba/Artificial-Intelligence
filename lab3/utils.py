# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:38:47 2020

@author: pocoloco
"""

from copy import deepcopy
  
def count_gene(individual, gene):
    count=0
    for tpl in individual:
        if tpl==gene:
            count+=1
            
    return count

def count_vertically(tuples, n):
    score=0
    for k in range(0,n):
        each=[]
        for tup in tuples:
            each.append(tup[k])
        score+=(len(each)-len(set(each)))
    return score

def all_swaps(permutation):
  alls=[]
  for i in range(len(permutation)-1):
    for j in range(i+1, len(permutation)):
      aux=deepcopy(permutation)
      elAux=aux[j]
      aux[j]=aux[i]
      aux[i]=elAux
      alls.append(aux)
  return alls

def get_distance(perm1, perm2):
    p1 = list(perm1)
    p2 = list(perm2)
    n=len(p1)
    dist=0
    for i in range(n):
        dist+=abs(p1[i]-p2[i])
    return dist