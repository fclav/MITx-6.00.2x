#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:03:31 2017

@author: fequi
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    numRed = 4
    numGreen = 4
    bucket = ["red"]*numRed + ["green"]*numGreen
    numDrawn = 3
    numConsecutiveDraws = 3
    
    trialHits = 0
    for k in range(numTrials):
        hits = 0
        for i in range(numConsecutiveDraws):
            drawn = random.sample(bucket, numDrawn)
            if drawn.count(drawn[0]) == numDrawn:
                hits += 1
            
        if hits == numConsecutiveDraws:
            trialHits += 1
    
    return trialHits / numTrials

def test():
    for numTrials in [10,100,1000,10000,100000]:
        prob = drawing_without_replacement_sim(numTrials)
        print("For numTrials =", str(numTrials), "estimated:",prob,"(expected 0.003)")
        
#test()