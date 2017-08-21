#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:03:10 2017

@author: fequi
"""
import numpy as np
import pylab

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    # Super slow and memory intensive but does the job
    choices = np.array(choices)
    numCombinations = 2**len(choices)
    combinations = []
    for i in range(numCombinations):
        binStr = bin(i)[2:]
        binStr = "0" * (len(choices) - len(binStr)) + binStr
        comb = np.array(list(map(lambda x: int(x), binStr)))
        combinations.append(comb)
        
    combinations.sort(key = lambda x: sum(x))
    bestSum = 0
    bestComb = combinations[0]
    for comb in combinations:
        combSum = sum(comb * choices)
        if combSum == total:
            return comb
        elif combSum < total and bestSum < combSum:
            bestSum = combSum
            bestComb = comb
    
    return bestComb
    
def test_find_combination():
    tests = []
    tests.append({"id":1, "choices":[1,2,2,3], "total":4, "output":[[0, 1, 1, 0], [1, 0, 0, 1]]})
    tests.append({"id":2, "choices":[1,1,3,5,3], "total":5, "output":[[0, 0, 0, 1, 0]]})
    tests.append({"id":3, "choices":[1,1,1,9], "total":4, "output":[[1, 1, 1, 0]]})
    
    for test in tests:
        result = find_combination(test["choices"], test["total"])
        if not result is None and list(result) in test["output"]:
            print("Test " + str(test["id"]) + ":", "PASS")
        else:
            print("Test " + str(test["id"]) + ":", "FAIL")