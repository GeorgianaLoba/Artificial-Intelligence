# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:44:31 2020

@author: Geo
"""
from domain import Graph, Ant
import random
import statistics

class ACO:
    def __init__(self, n, nr_ants, trace, evaporation):
        self.__n = n
        self.__colony_size= nr_ants
        self.__graph = Graph()
        self.__graph.generate_graph(n)
        self.__evaporation = evaporation
        self.__colony = [Ant(n, trace, self.__graph, random.choice(self.__graph.get_nodes())) for _ in range(nr_ants)]

     
    def best_ant(self):
        """
            Returns the ant that has the best fitness (the smaller, the better).
            Also returns the fitness itself of the best ant
        """
        fitnesses = [a.fitness() for a in self.__colony]
        best_fitness = min(fitnesses)
        for ant in self.__colony:
            if ant.fitness() == best_fitness:
                return ant, best_fitness



    def get_average_fitness(self):
        """
            Computes the average of ants' fitnesses
        """
        return statistics.mean([ant.fitness() for ant in self.__colony])

    def get_standard_deviation(self):
        """
            Computes the standard deviation
        """
        return round(statistics.stdev([ant.fitness() for ant in self.__colony]), 2)

 
    def one_step_all(self):
        """
            All ants perform one step. Then we evaporate some trace/smell from the edges
        """
        for current_ant in self.__colony:
            if not current_ant.finished_walk():
                current_ant.one_step()
        self.evaporate()

        
    def evaporate(self):
        """
            After an ant finished its walk, some pheromones will evaporate.
            Coefficient of evaporation of the pheromones is given as self.__trace

        """
        for node in self.__graph.get_nodes(): #all nodes of the graph, one by one
            for neighbour in self.__graph.get_outbound(node): #all nodes except the one given as parameter
                if self.__graph.get_weight(node,neighbour)!=0:
                    evaporation = self.__graph.get_weight(node, neighbour) *self.__evaporation /100
                    weight = self.__graph.get_weight(node, neighbour) - evaporation
                    if weight>=0:
                        self.__graph.set_weight(node, neighbour, weight)
                    else:
                        self.__graph.set_weight(node, neighbour, 0)
            for neighbour in self.__graph.get_inbound(node): #all nodes except the one given as parameter
                if self.__graph.get_weight(neighbour, node)!=0:
                    evaporation = self.__graph.get_weight(neighbour,node) *self.__evaporation /100
                    weight = self.__graph.get_weight(neighbour,node) - evaporation
                    if weight>=0:
                        self.__graph.set_weight(neighbour,node, weight)
                    else:
                        self.__graph.set_weight(neighbour,node, 0)
