# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:42:20 2019

@author: aishw
"""

import math

def sig(x):
    
    #use logistic function as activation function
    return 1/ float(1 + math.exp(-x))
    raise Exception('Implement this part.')
def inv_sig(x):
    #derivative of the output of neruon with respect to its input
    return sig(x) * (1 - sig(x))
    raise Exception('Implement this part.')
def err(o, t):
    #squared error function, o is the actual output value and t is the target output
    return 0.5 * ((t - o) ** 2)
    raise Exception('Implement this part.')
def inv_err(o, t):
    #derivative of squared error function with respect to o
    return (o - t)
    raise Exception('Implement this part.')

