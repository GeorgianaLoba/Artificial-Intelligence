# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:36:37 2020

@author: GeoLoba
"""
import random
import numpy
from utils import count_gene

class Individual:
    def __init__(self, n):
        self.__n=n
        self.__individual = self.__create_individual()
        
        
    def __create_individual(self):
        individ=[]
        for i in range(2*self.__n):
            permutation=numpy.random.permutation(self.__n) #if n=3 -> will give [2,0,1]
            for j in range(len(permutation)):
                permutation[j]=permutation[j]+1
            individ.append(tuple(permutation))
        return individ
            
    def get_individual(self):
        return self.__individual[:]
    
    def set_individual(self, new_individual):
        self.__individual=new_individual[:]
    
    def get_n(self):
        return self.__n
    
    
    def mutate(self): #swap mutation
        genes=random.sample(range(0, self.__n), 2)
        gene1=genes[0]
        gene2=genes[1]
        values = self.get_individual()
        aux=values[gene1]
        values[gene1]=values[gene2]
        values[gene2]=aux
        self.set_individual(values)
        return self    
    
    def crossover(self, other):
        n=self.__n
        p1= self.get_individual()
        p2=other.get_individual()
        genes=random.sample(range(0, n), 2)
        genes.sort()
        gene1=genes[0]
        gene2=genes[1]
        offspring = [tuple(x) for x in numpy.zeros((2*n,n),int)] 
        for i in range(gene1, gene2+1):
            offspring[i]=p1[i]
        for i in range(0, gene1):
            offspring[i]=p2[i]
        for i in range(gene2+1, 2*n):
            offspring[i]=p2[i]
        our_offspring = Individual(n)
        our_offspring.set_individual(offspring)
        return our_offspring   
    
    def fitness(self):
        ind = self.__individual
        score=0
        for tpl in ind: #count dubplicate permutations
            score+=count_gene(ind, tpl) #-1 because for sure, it's at least once present
            score-=1 
        n=len(ind)//2
        for i in range(n):
            l=[]
            for j in range(n):
                l.append(ind[j][i])
            score+=len(l)-len(set(l))
        for j in range(n):
            l=[]
            for i in range(n, 2*n):
                l.append(ind[i][j])
            score+=len(l)-len(set(l))
        l=[] #dublicates
        for i in range(n):
            j=n+i
            for k in range(n):
                l.append((ind[i][k],ind[j][k]))
        score+=len(l)-len(set(l))     
        return score
    
    
    def __str__(self) -> str:
      finished=""
      for tuple in self.__individual:
        finished+=str(tuple)
        finished+="\n"
      return finished
  
    
    
class Particle:
    def __init__(self, n):
        self.__n=n
        self.__individual=self.__create_individual()
        self.__personal_best = self.fitness()
        self.__velocity = [0 for i in range(2*n)]
        self.__best_particle = self.__individual.copy()
      
        
    def __create_individual(self):
        individ=[]
        for i in range(2*self.__n):
            permutation=numpy.random.permutation(self.__n) #if n=3 -> will give [2,0,1]
            for j in range(len(permutation)):
                permutation[j]=permutation[j]+1
            individ.append(tuple(permutation))
        return individ
            
    def fitness(self):
        ind = self.__individual
        score=0
        for tpl in ind: #count dubplicate permutations
            score+=count_gene(ind, tpl) #-1 because for sure, it's at least once present
            score-=1 
        n=len(ind)//2
        for i in range(n):
            l=[]
            for j in range(n):
                l.append(ind[j][i])
            score+=len(l)-len(set(l))
        for j in range(n):
            l=[]
            for i in range(n, 2*n):
                l.append(ind[i][j])
            score+=len(l)-len(set(l))
        l=[] #dublicates
        for i in range(n):
            j=n+i
            for k in range(n):
                l.append((ind[i][k],ind[j][k]))
        score+=len(l)-len(set(l))     
        return score   
 
    def get_n(self):
        return self.__n
 
    def get_personal_best(self):
        return self.__personal_best
    
    def set_personal_best(self, new_personal_best):
        self.__personal_best=new_personal_best
        
    def set_velocity(self, new_velocity):
        self.__velocity=new_velocity

    def get_velocity(self):
        return self.__velocity
                
    def get_individual(self):
        return self.__individual[:]
    
    def set_individual(self, new_individual):
        self.__individual=new_individual.copy()
        if self.fitness() > self.__personal_best:
            self.__personal_best = self.fitness()
        #TODO not sure
    
    def get_best_particle(self):
        return self.__best_particle
    
    def __str__(self) -> str:
      finished=""
      for tuple in self.__individual:
        finished+=str(tuple)
        finished+="\n"
      return finished