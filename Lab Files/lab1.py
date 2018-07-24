'''
Created on Sep 7, 2017

@author: brand
'''
"""I pledge that I have abided by the Steven's Honor System-Brandon Soong"""
from cs115 import map, reduce
from math import factorial
import math

def inverse(n):
    """Sets the n value over 1"""
    return 1/n

def e(n):
    """Creates a range from 1 - the nth term, and using the factorial function creates a list.
     Then the  return statement is +1 to get the correct value, and the sum of the inverse and the list 
     create the Taylor function of e"""
    elst = range(1,n+1)
    elstwo = map(factorial,elst)
    return 1 + sum(map(inverse, elstwo))

def error(n):
    """Creates the function error and gives an increasingly smaller amount"""
    return abs(e(n)- math.e)

