# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:53:53 2020

@author: Geo
"""

from problem import ACO

class Controller:
    def __init__(self, n, colony_size, trace, evaporation):
        self.__n = n
        self.__colony_size = colony_size
        self.__problem = ACO(n, colony_size, trace, evaporation)
        self.__generation = 0
        
    
    def get_standard_deviation(self):   
        return self.__problem.get_standard_deviation()        
        
    def get_average_fitness(self):
        return self.__problem.get_average_fitness()
    
    def solution(self):
        """
            Returns the ant that has the best fitness
        """
        return self.__problem.best_ant()
        
    def algorithm(self):
        """
            All ants will finish their walk over the graph by calling iteratively
            the one_step_for_all function
        """
        for i in range(self.__n*2):
            self.__problem.one_step_all()
            
        