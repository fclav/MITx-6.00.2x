#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:42:49 2017

@author: fequi
"""
import random
import statistics
import pylab

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def copy(self):
        return Point(self.x, self.y)
    def norm(self):
        return (self.x**2 + self.y**2)
    def distance(self):
        return (self.norm())**0.5

def walk_step(start, unit=1):
    direction = random.randrange(0,4)
    if direction % 2 == 0:
        # Go up or down
        if direction == 0:
            # Go up
            start.y += unit
        else:
            # Go down
            start.y -= unit
    else:
        # Go right or left
        if direction == 1:
            # Go right
            start.x += unit
        else:
            # Go left
            start.x -= unit
    return

def random_walk(steps, unit=1, debug=False):
    position = Point()
    for i in range(steps):
        walk_step(position, unit)
        if debug:
            print(i,",", position.distance())
    return position

def test_random_walk(unit=1):
    samples = 100
    data = { "steps" : [], "mean" : [], "stdev" : [] }
    for steps in [1, 10, 100, 500, 1000, 5000]:
        runs = []
        data["steps"].append(steps)
        for k in range(samples):
            distance = random_walk(steps, unit).distance()
            runs.append(distance)
        
        mean = statistics.mean(runs)
        stdev = statistics.stdev(runs)
        data["mean"].append(mean)
        data["stdev"].append(stdev)
    
    pylab.plot(data["steps"], data["mean"])