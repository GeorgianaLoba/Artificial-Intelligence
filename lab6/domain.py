# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:30:57 2020

@author: Geo
"""


header = ["leftWeight", "leftDistance", "rightWeight","rightDistance"]



def class_counts(rows):
    # Counts the number of each type of class in a dataset.
    stats = {}
    
    for row in rows:
        classLabel = row[0] 
        if classLabel not in stats:
            stats[classLabel] = 0
        stats[classLabel] += 1
    
    return stats



class Inquire:
    def __init__(self, column, value):
        self.column = column 
        self.value = value
        
    def match(self, example):
        val = example[self.column]
        if isinstance(val, int):
            return val>=self.value
        elif isinstance(val, float):
            return val>=self.value
        else:
            return val==self.value
        
    def __str__(self)->str:
        if isinstance(self.value, int):
            condition=">="
        elif isinstance(self.value, float):
            condition=">="
        else:
            condition="=="
        build="Is " + header[self.column]+" "
        build+=condition
        build+=" "
        build+=str(self.value)
        return build


class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)


class DecisionTree:
    def __init__(self, inquire, true_branch, false_branch):
        self.inquire = inquire
        self.true_branch = true_branch
        self.false_branch = false_branch
        
        