#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:26:15 2017

@author: fequi
"""
import random
import numpy as np

def pi_mc(num_samples = 1000):
    """
    Estimates the value of PI using a Monte Carlo method using
    num_samples samples.
    """
    hits = 0
    for i in range(num_samples):
        x = random.random() * np.pi
        y = random.random()
        r = (x**2 + y**2)**0.5
        if r <= 1:
            hits += 1
    area = hits / num_samples
    pi = 4*area
    return pi


def test_pi_mc(num_samples = 1000, num_samples_per_pi = 1000):
    """
    Calculates the uncertainty of estimating PI using the function pi_mc
    by calling it num_samples times of num_samples_per_pi tries each
    and averaging the results.
    """
    pis = []
    for i in range(num_samples):
        pis.append(pi_mc(num_samples_per_pi))
    mean = np.mean(pis)
    stdev = np.std(pis)
    print("pi =", str(mean),"+-",str(stdev))


def int_sin_0_pi(num_samples = 1000): 
    """
    Estimates the value of the integral of sin(x) from 0 to PI 
    using a Monte Carlo method with num_samples samples.
    """
    hits = 0
    for i in range(num_samples):
        x = random.random() * np.pi
        y = random.random()
        if y <= np.sin(x):
            hits += 1
    prob = hits / num_samples
    integral = np.pi * prob
    return integral

def test_int_sin(num_samples = 1000, num_samples_per_mc = 1000):
    """
    Calculates the uncertainty of estimating integral of sin(x) from 0 to PI
    using the function int_sin_0_pi by calling it num_samples times with 
    num_samples_per_mc tries each
    and averaging the results.
    """
    pis = []
    for i in range(num_samples):
        pis.append(int_sin_0_pi(num_samples_per_mc))
    mean = np.mean(pis)
    stdev = np.std(pis)
    print("int from 0 to PI sin(x)dx =", str(mean),"+-",str(stdev))