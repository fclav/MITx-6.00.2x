#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:42:46 2017

@author: fequi
"""

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    birthProb = 1.0 - CURRENTRABBITPOP/MAXRABBITPOP
    if random.random() < birthProb:
        CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    hasEaten = False
    if CURRENTRABBITPOP > 10:
        huntProb = CURRENTRABBITPOP / MAXRABBITPOP
        if random.random() < huntProb:
            hasEaten = True
    
    if hasEaten:
        birthProb = 1/3
        if random.random() < birthProb:
            CURRENTFOXPOP += 1
    elif CURRENTFOXPOP > 10:
        deathProb = 1/10
        if random.random() < deathProb:
            CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbitPop = []
    foxPop = []
    for t in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPop.append(CURRENTRABBITPOP)
        foxPop.append(CURRENTFOXPOP)
    return (rabbitPop, foxPop)


def test_simulation(numSteps):
    data = runSimulation(numSteps)
    pylab.plot(data[0], label = "rabbits")
    pylab.plot(data[1], label = "foxes")
    pylab.xlabel("Timestep")
    pylab.ylabel("Population count")
    pylab.legend()
    pylab.title("Evolution of the populations of rabbits and foxes")
    pylab.show()


def test_polyfit():
#    CURRENTRABBITPOP = 50
#    CURRENTFOXPOP = 300
    numSteps = 200
    data = runSimulation(numSteps)
    
    x = pylab.arange(numSteps)    
    fitRabbits = pylab.polyfit(x, data[0], 2)
    fitFoxes = pylab.polyfit(x, data[1], 2)
    valRabbits = pylab.polyval(fitRabbits, x)
    valFoxes = pylab.polyval(fitFoxes, x)
    
#    pylab.plot(data[0], label = "rabbits")
    pylab.plot(valRabbits, '-', label = "rabbit fit")
#    pylab.plot(data[1], label = "foxes")
    pylab.plot(valFoxes, '-', label = "fox fit")
    
    x2 = pylab.arange(numSteps * 10)
    futureRabbits = pylab.polyval(fitRabbits, x2)
    futureFoxes = pylab.polyval(fitFoxes, x2)
    
    pylab.plot(futureRabbits, '--', label = "rabbit tendency")
    pylab.plot(futureFoxes, '--', label = "fox tendency")
    
    pylab.xlabel("Timestep")
    pylab.ylabel("Population count")
    pylab.legend()
    pylab.title("Evolution of the populations of rabbits and foxes")
    pylab.show()

#test_simulatiosn(200)
test_polyfit()