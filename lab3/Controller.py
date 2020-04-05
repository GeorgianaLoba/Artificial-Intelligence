# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:24:55 2020

@author: GeoLoba
"""

from utils import get_distance, all_swaps
from Domain import Individual
from Repository import PSOPopulation, EAPopulation
import random
from copy import deepcopy
import statistics

class EA:
    def __init__(self, nr_generations, mutation, population_size, n):
        self.__repository=EAPopulation(population_size, n)
        self.__mutation= mutation
        self.__nr_generations=nr_generations

    def get_mutation(self):
        return self.__mutation
     
    def set_mutation(self, mutation):
        self.__mutation = mutation
        
    def get_population_size(self):
        return self.__population_size
        
    def set_population_size(self, population_size):
        self.__population_size= population_size

    def get_repository(self):
        return self.__repository
    
    def set_nr_generations(self, nr_generations):
        self.__nr_generations=nr_generations
    
    def get_nr_generations(self):
        return self.__nr_generations

    def create_map_population(self, population, mean_fitness):
        pop={}
        for individ in population:
            pop[individ]=(individ.fitness()/mean_fitness)
        return pop
            
    def roulette_sorting(self, population):
        sum=0
        for individ in population:
             sum+=individ.fitness()
        meanFitness=sum/len(population)
        population_dictionary=self.create_map_population(population, meanFitness)
        new_population=[k for k,v in sorted(population_dictionary.items() , key=lambda x: x[1])]
        return new_population[:self.__repository.get_population_size()]
   
         
    def new_generation(self): #survival selection
        population=self.__repository.get_population()
        new_population = self.__repository.get_population()
        for i in range(0, len(population)-1, 2): #get n/2 children
            offspring=population[i].crossover(population[i+1])
            if random.random()>self.__mutation:
                new_offspring=offspring.mutate()
                new_population.append(new_offspring)
            else:
                new_population.append(offspring)
        self.__repository.set_population(self.roulette_sorting(new_population))
        
        fitnesses=[]
        for ind in self.__repository.get_population():
            fitnesses.append(ind.fitness())
        standard_deviation = round(statistics.stdev(fitnesses),3)
        average = round(statistics.mean(fitnesses),3)
        return standard_deviation, average


    def is_solution(self):
        #if self.fitness(self.__repository.get_population()[0])==0:
        if self.__repository.get_population()[0].fitness()==0:
            return True
        else:
            return False
        
class HC:
    def __init__(self, n):
        self.__individual= Individual(n)
        self.__n = n

    def get_individual(self):
        return self.__individual
    
    def set_individual(self, new_individual):
        self.__individual= new_individual


    def get_neighbours(self, individual): #for HC
        #get a list of neighbours of a specific individual by swaping 2 elems 
        #in each permutation; given example by prof: [1,4,2,3] will be =>
        #(4,1,2,3), (2,4,1,3), (3,4,2,1), (1,2,4,3), (1,3,2,4),(1,4,3,2)
        #do the same for every tuple in the individual
        #return the population afterwards
        neighbours=[]
        current=individual.get_individual()
        for i in range(len(current)):
            all_perm = all_swaps(list(current[i]))
            for perm in all_perm:
                aux=deepcopy(current)
                aux[i]=tuple(perm)
                neighbours.append(aux)
        new_population=[]
        for neighbour in neighbours:
           individ=Individual(self.__n)
           individ.set_individual(neighbour)
           new_population.append(individ)
        return new_population
    
    
    def create_map_population(self, population, mean_fitness):
        pop={}
        for individ in population:
            pop[individ]=(individ.fitness()/mean_fitness)
            #pop[individ]= (self.fitness(individ) / mean_fitness)
        return pop
        
    def roulette_sorting(self, population):
        sum=0
        for individ in population:
             sum+=individ.fitness()
        meanFitness=sum/len(population)
        population_dictionary=self.create_map_population(population, meanFitness)
        new_population=[k for k,v in sorted(population_dictionary.items() , key=lambda x: x[1])]
        return new_population
    
    def new_generation(self):
        current=self.__individual;
        generated_neighbours = self.get_neighbours(current)
        sorted_neighbours=self.roulette_sorting(generated_neighbours)
        #current_fitness= self.fitness(population[0])
        #new_best_fitness = self.fitness(sorted_neighbours[0])
        current_fitness=current.fitness()
        new_best_fitness=sorted_neighbours[0].fitness()
        
        fitnesses=[]
        for ind in sorted_neighbours:
            fitnesses.append(ind.fitness())
        
        standard_deviation = round(statistics.stdev(fitnesses),3)
        average = round(statistics.mean(fitnesses),3)
    
        
        if new_best_fitness<current_fitness:
            self.set_individual(sorted_neighbours[0])
            return 0, standard_deviation, average
        else:
            return -1, standard_deviation, average

    def is_solution(self):
        #if self.fitness(self.__repository.get_population()[0])==0:
        if self.__individual.fitness()==0:
            return True
        else:
            return False
class PSO:
    def __init__(self, population_size, neighborhood_size,n, w, c1, c2):
        self.__repository=PSOPopulation(population_size, n)
        self.__population_size = population_size
        self.__neighborhood_size = neighborhood_size
        self.__w=w
        self.__c1=c1
        self.__c2=c2

    def get_population_size(self):
        return self.__population_size
        
    def set_population_size(self, population_size):
        self.__population_size= population_size

    def get_repository(self):
        return self.__repository
    
    def get_neighborhood_size(self):
        return self.__neighborhood_size
    
    def set_neighborhood_size(self, new_neighborhood_size):
        self.__neighborhood_size=new_neighborhood_size
        
    def get_w(self):
        return self.__w
    
    def get_c1(self):
        return self.__c1
    
    def get_c2(self):
        return self.__c2
    
    def get_best_neighbors(self, hoods):
        population = self.__repository.get_population()
        best=[]
        for i in range(len(hoods)):
            best.append(hoods[i][0])
            for j in range(1, len(hoods[i])):
                if population[best[i]].fitness()>population[hoods[i][j]].fitness():
                    best[i]=hoods[i][j]
        return best
    
    def update_velocity(self, best):
        population = self.__repository.get_population()
        for i in range(len(population)):
            for j in range(len(population[0].get_velocity())):
                new_velocity = self.__w * population[i].get_velocity()[j]
                new_velocity = new_velocity + self.__c1* random.random()*get_distance(population[best[i]].get_individual()[j],population[i].get_individual()[j])
                new_velocity=  new_velocity + self.__c2*random.random()*get_distance(population[i].get_best_particle()[j], population[i].get_individual()[j])
                current = population[i].get_velocity().copy()
                current[j]=new_velocity
                population[i].set_velocity(current)
        
    def update_position(self, best):
        population=self.__repository.get_population()
        for i in range(len(population)):
            new=[]
            for j in range(len(population[0].get_velocity())):
                if random.random() < population[i].get_velocity()[j]:
                    new.append(population[best[i]].get_best_particle()[j])
                else:
                    new.append(population[i].get_individual()[j])
            population[i].set_individual(new)
            
                 
    def iteration(self): #w,c1,c2 are constant
        neighbours = self.__repository.get_neighbourhoods(self.__neighborhood_size)
        best_neighbors = self.get_best_neighbors(neighbours)
        self.update_velocity(best_neighbors)
        self.update_position(best_neighbors)
        fitnesses=[]
        for ind in self.__repository.get_population():
            fitnesses.append(ind.fitness())
        standard_deviation = round(statistics.stdev(fitnesses),3)
        average = round(statistics.mean(fitnesses),3)
        return standard_deviation, average
        

        
        
        
        
        