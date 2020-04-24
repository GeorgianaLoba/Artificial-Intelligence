# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:49:12 2020

@author: Geo
"""

from typing import List
from domain import DecisionTree, Leaf, Inquire, class_counts
Dataset = List[List]


def classify(row, decisionTree):
    # Base case: we've reached a leaf
    if isinstance(decisionTree, Leaf):
        return decisionTree.predictions
    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if decisionTree.inquire.match(row):
        return classify(row, decisionTree.true_branch)
    else:
        return classify(row, decisionTree.false_branch)
    
def gini(rows):
    """
        Calculate the Gini Impurity for given group.
    """
    counts = class_counts(rows)
    impurity = 1
    for label in counts:
        prob_of_lbl = counts[label] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def information_gain(left, right, current_uncertainty):
    """
        Information gain is obtained by splitting the dataset into `left` and `right`.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


def find_best_split(rows):
    """
        Find the best question to ask by iterating over every
        feature / value and calculating the information gain.
    """
    best_gain, best_inquire = 0, None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  # number of feature columns

    for col in range(n_features):
        values = set([row[col] for row in rows])
        for val in values:
            inquire = Inquire(col, val)
            true_rows, false_rows = partition(rows, inquire)
            # Skip this split if it doesn't divide the dataset
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue
            # Calculate the information gain from this split
            gain = information_gain(true_rows, false_rows, current_uncertainty)
            if gain > best_gain:
                best_gain, best_inquire = gain, inquire

    return best_gain, best_inquire

def partition(rows, inquire):
    """
        split into partitions based on the answers of the inquire
    """
    trueRows = []
    falseRows = []
    for row in rows:
        if inquire.match(row):
            trueRows.append(row)
        else:
            falseRows.append(row)
            
    return trueRows,falseRows


def build_tree(rows):
    """
        Building a tree recursively for the given dataset
        That dataset is continously split until no further information
        can be obtained
    """
    gain, inquire = find_best_split(rows)

    if gain == 0:
        # No further splits are possible
        return Leaf(rows)
    true_rows, false_rows = partition(rows, inquire)
    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)
    return DecisionTree(inquire, true_branch, false_branch)
