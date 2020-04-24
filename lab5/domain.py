# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:33:25 2020

@author: Geo
"""
import random
import itertools

class Ant:
    def __init__(self, n, trace, graph, start_node):
        self.__n= n
        self.__trace=trace
        self.__graph=graph
        self.__current_node = start_node
        self.__visited = []
        self.__visited.append(start_node)
        
    def one_step(self):
        """
            The ant makes a move inside the graph. It iterates through its neighbours
            in order to find the best one and try to go there as well. 
            The weight represent the pheromones on that edge. More pheromones, better.
            The ant moves considering both the best neighbour and the rest of the nodes 
            in the graph (given a percentage, in my case 50%).
            After chosing the path (=edge) of the ant, update the visited nodes list
            and also update the graph, adding to that specific edge a trace
        """
        best_friend = None
        best_weight = float('inf')
        neighbours_out = self.__graph.get_outbound(self.__current_node)
        for neighbour in neighbours_out:
            weight = self.__graph.get_weight(self.__current_node, neighbour)
            if  weight < best_weight:
                best_weight = weight
                best_friend =neighbour
        
        neighbours_in= self.__graph.get_inbound(self.__current_node)
        for neighbour in neighbours_in:
            weight = self.__graph.get_weight(neighbour, self.__current_node)
            if  weight < best_weight:
                best_weight = weight
                best_friend =neighbour
        """
            Here I asked a friend. He said that basically we give like 50-50 changes
            for the ant to choose either its best neighbour or go randomly to another
            node in the graph. The best neighbour is similar to a local optima.
        """
        if random.random() > 0.5 and best_friend is not None:
            self.__visited.append(best_friend)
            self.__current_node = best_friend 
        else:
            neighbours = neighbours_in+neighbours_out
            if len(neighbours)>0:
                self.__current_node = random.choice(neighbours)
                self.__visited.append(self.__current_node)
            
        self.add_smell()


    def add_smell(self):
        """
            Add a pheromon trail to the 'road' from the penultimate node of 
            the visited list to the ultimate node of that list. The trace after
            each passing of an ant is given as self.__trace
        """
        from_node = self.__visited[len(self.__visited)-2]      
        to_node = self.__visited[len(self.__visited)-1]
        initial_smell = self.__graph.get_weight(from_node, to_node)
        if initial_smell is None:
            initial_smell = self.__graph.get_weight(to_node, from_node)

        self.__graph.set_weight(from_node, to_node, initial_smell+self.__trace)

    
    @staticmethod
    def count_gene(individual, gene):
        count=0
        for tpl in individual:
            if tpl==gene:
                count+=1
        return count


    def fitness(self):
        """
            Computes a score based on the visited list of nodes, the smaller the better
        """
        ind = self.__visited
        score=0
        for tpl in ind: #count dubplicate permutations
            score+=Ant.count_gene(ind, tpl) #-1 because for sure, it's at least once present
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


    def finished_walk(self):
        return len(self.__visited )== self.__n*2
    
    
    def __str__(self)->str:
        builded=""
        for node in self.__visited:
            builded+=str(node)
            builded+="\n"
        return builded
    

class Graph:
    def __init__(self):
        """
            The graph is a dictionary {k: v} where
                k = tuple of 2 nodes representing and edge
                v = weight of the edge        
        """
        self.__graph = {}
        
    def generate_graph(self, n):
        """
            If size of permutation is n, we have n! possible permutations = nodes
            The graph is complete, with n! nodes => n(n-1)/2 edges
            Each edge has its weight initialised with 0
        """
        perms = list(itertools.permutations(range(1, n + 1)))
        for i in range(len(perms)-1):
            for j in range(i+1,len(perms)):
                key=(perms[i], perms[j])
                if key not in self.__graph.keys():
                    self.__graph[key] = 0
                
                
    def get_graph(self):
        """ 
            Returns the graph (the dictionary)
        """
        return self.__graph
                
    def get_weight(self, node1, node2):
        """
            Get the weight of the edge
        """
        tpl = (node1, node2)
        if tpl in self.__graph.keys():
            return self.__graph[tpl]
    

    def set_weight(self, node1, node2, weight):
        """
            Set the weight of the edge
        """
        tpl = (node1, node2)
        if tpl in self.__graph.keys():
            self.__graph[tpl] = weight
    
    def get_nodes(self):
        """
            Return all the nodes of the graph as a list
        """
        nodes = []
        for key in self.__graph.keys():
            if key[0] not in nodes:
                nodes.append(key[0])
            if key[1] not in nodes:
                nodes.append(key[1])
        return nodes

    def get_outbound(self, node):
        """
            Get all outbounds of a node
        """
        friends = []
        for key in self.__graph.keys():
            if node==key[0] and key[1] not in friends and key[1]!=node:
                friends.append(key[1])
        return friends
    
    def get_inbound(self, node):
        """
            Get all inbounds of a node
        """
        friends = []
        for key in self.__graph.keys():
            if node == key[1] and key[0] not in friends and key[0]!=node:
                friends.append(key[0])
        return friends

    def __str__(self)->str:
        builded=""
        for key in self.__graph.keys():
            builded+=str(key)
            builded+=": "
            builded+=str(self.__graph[key])
            builded+="\n"
        return builded
        
