# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:36:54 2020

@author: GeoLoba
"""

from Domain import Individual, Particle
from random import randint


class EAPopulation:
    def __init__(self, population_size, n):
        self.__population_size=population_size
        self.__n=n
        self.__population=self.create_population()
        
        
    def create_population(self):    
        #simply creates a population of individuals and return it
        population=[]
        for i in range(self.__population_size):
            individual=Individual(self.__n)
            population.append(individual)
        return population  

    def get_population(self):
        return self.__population[:]
    
    def set_population(self, new_population):
        self.__population=new_population
    
    def get_population_size(self):
        return self.__population_size

    def get_n(self):
        return self.__n


class PSOPopulation:
    def __init__(self, population_size, n):
        self.__population_size=population_size
        self.__n=n
        self.__population=self.create_population()


    def create_population(self):    
        #simply creates a population of individuals and return it
        population=[]
        for i in range(self.__population_size):
            individual=Particle(self.__n)
            population.append(individual)
        return population  

    def get_population(self):
        return self.__population[:]
    
    def set_population(self, new_population):
        self.__population=new_population
    
    def get_population_size(self):
        return self.__population_size

    def get_n(self):
        return self.__n


    def get_neighbourhoods(self, neighbourhoodSize):
        if self.__population_size<neighbourhoodSize:
            neighbourhoodSize=self.__population_size
        
        neighbourhoods=[]
        for i in range(self.__population_size):
            one=[]
            for j in range(neighbourhoodSize):
                x=randint(0, self.__population_size-1)
                while (x in one):
                    x=randint(0, self.__population_size-1)
                one.append(x)
            neighbourhoods.append(one.copy())
        return neighbourhoods    



