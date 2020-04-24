# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:03:45 2020

@author: Geo
"""


"""

!!!!! inspiration here:
    https://github.com/random-forests/tutorials/blob/master/decision_tree.py
    https://github.com/random-forests/tutorials/blob/master/decision_tree.ipynb
    https://www.youtube.com/watch?v=LDRbO9a6XPU&feature=youtu.be
"""

import operator
from math import floor
from random import shuffle
import numpy as np
from utils import build_tree, classify

def readData(file_path):
    f = open(file_path, "r")
    ds = []
    for line in f:
        values = line.strip('\n').split(',')
        values[1] = int(values[1])
        values[2] = int(values[2])
        values[3] = int(values[3])
        values[4] = int(values[4])
        ds.append(values)
    f.close()
    return ds

def split_train_test(data_set, p):
    """
        Dataset is split into train and test
        In case p=1, train and test are both the initial dataset
    """
    if p == 1:
        return data_set, data_set
    data_set_len = len(data_set)
    train_split = floor(p * data_set_len)
    shuffle(data_set)
    return data_set[:train_split], data_set[train_split:]


if __name__ == '__main__':
    """
        If we use the entire set to train we will get maximum accuracy
        Splitting the dataset will will decrease the accuracy
    """
    accuracy = float(input("Enter the accuracy of prediction you desire: "))
    data_set = readData('dataset.data')
    train, test = split_train_test(data_set, accuracy)
    tree = build_tree(data_set)
    good_B = 0
    good_R = 0
    good_L = 0
    for row in train:
        prediction = classify(row, tree)
        letter = max(prediction.items(), key=operator.itemgetter(1))[0]
         
        if row[0] == letter and row[0]=='L':
            good_L+=1
            
        if row[0] == letter and row[0]=='B':
            good_B+=1
        
        if row[0] == letter and row[0]=='R':
            good_R+=1
 #=============================================================================
    print(good_L," out of 288 left")     
    print(good_L," out of 288 right")
    print(good_B," out of 49 balanced")
    print("The ones left are not correctly predicted")
# =============================================================================
   
    
