#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:33:56 2017

@author: fequi
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    maxSum = L[0]
    for initIndex in range(0, len(L)):
        for endIndex in range(initIndex, len(L)):
            indexSum = sum(L[initIndex:endIndex+1])
            maxSum = indexSum if maxSum < indexSum else maxSum
    return maxSum
    
    
def test_solution():
    tests = []
    tests.append({"id":1, "input":[3, 4, -1, 5, -4], "output":11})
    tests.append({"id":2, "input":[3, 4, -8, 15, -1, 2], "output":16})
    
    for test in tests:
        print("Test",test["id"])
        output = max_contig_sum(test["input"])
        print("Returned:", output)
        print("Expected:", test["output"])
    
#test_solution()