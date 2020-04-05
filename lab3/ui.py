# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:06:05 2020

@author: GeoLoba
"""
from Controller import EA, HC, PSO
import matplotlib.pyplot as plt
import matplotlib

print("for testing...")
print("1 EA; 2 HC; 3 PSO")
inp=int(input())
if inp == 1:
    number_generations = 30
    n = 4
    mutation= 0.1
    population_size = 1000
    controller = EA(number_generations, mutation, population_size, n)
    fitnesses=[]
    trials=[]
    trial = 0
    for i in range(number_generations):
        deviation, average=controller.new_generation()
        print("Deviation: "+ str(deviation))
        print("Average: "+ str(average))
        if controller.is_solution()== True:
            print('Solution: ')
            print(controller.get_repository().get_population()[0])
            break
        if trial<30:
            fitnesses.append(controller.get_repository().get_population()[0].fitness())
            trials.append(trial)
            trial+=1
                
        print("Currently " + str(i) + " not reached a solution: ")
        print(controller.get_repository().get_population()[0])
    fix,ax=plt.subplots()
    ax.plot(trials, fitnesses)
    ax.set(xlabel="fitnesses", ylabel="trials", title="EA")
    ax.grid()
    plt.show()
    
if inp==2:
    number_generations = 100
    n = 4
    controller = HC(n)
    fitnesses=[]
    trials=[]
    trial = 0
    for i in range(number_generations):
        out, deviation, average=controller.new_generation()
        print("Deviation: "+ str(deviation))
        print("Average: "+ str(average))
        if controller.is_solution()== True:
            print('Solution: ')
            print(controller.get_individual())
            break
        if out == -1:
            print('Local optima reached: ')
            print(controller.get_individual())
            break
        if trial<30:
            fitnesses.append(controller.get_individual().fitness())
            trials.append(trial)
            trial+=1
        print("Currently " + str(i) + " not solution: ")
        print(controller.get_individual())
    fix,ax=plt.subplots()
    ax.plot(trials, fitnesses)
    ax.set(xlabel="fitnesses", ylabel="trials", title="EA")
    ax.grid()
    plt.show()   
if inp==3:
    number_generations = 100
    n =4
    population_size=10
    w=1.0
    c1=1.2
    c2=0.7
    neigh_size = 2
    fitnesses=[]
    trials=[]
    trial = 0
    controller=PSO(population_size,neigh_size, n, w, c1,c2)
    for i in range(number_generations):
        deviation, average=controller.iteration()
        print("Deviation: "+ str(deviation))
        print("Average: "+ str(average))
        if trial<30:
            fitnesses.append(controller.get_repository().get_population()[0].fitness())
            trials.append(trial)
            trial+=1
    best = 0 
    population = controller.get_repository().get_population()
    for i in range(population_size):
        if (population[i].fitness()<population[best].fitness()):
            best= i 
    print('Current best: ')
    print(population[best])
    fix,ax=plt.subplots()
    ax.plot(trials, fitnesses)
    ax.set(xlabel="fitnesses", ylabel="trials", title="EA")
    ax.grid()
    plt.show()   