# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:57:08 2020

@author: Geo
"""

from controller import Controller

class Console:
       
    def __init__(self):
        pass
    
    def run(self):
        print('Hello...')
        n = int(input("Give n: "))
        colony_size = int(input("Give the colony size: "))
        trace = int(input("Give trace: "))
        evaporation = int(input("Give evaporation percentage: "))
        controller = Controller(n, colony_size, trace, evaporation)
        
        controller.algorithm()
        best_ant, best_fitness =  controller.solution()
            
        if best_fitness == 0:
            print("\nFound solution... ")
        else:
            print("\nDidn't find a solution... ")
        print(best_ant)
        print(best_fitness)
            
        deviation = controller.get_standard_deviation()
        average = controller.get_average_fitness()
        print("Deviation is: " + str(deviation))
        print("Average Fitness is: " + str(average))
        
console = Console()
console.run()