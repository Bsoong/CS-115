'''
Created on Sep 14, 2017

@author: brand
'''
from cs115 import map, reduce
"""Multiply fuction to get a value"""
def mult(x,y):
    return x*y
"""Adds two numbers together"""
def add(x,y):
    return x+y
"""multiplies L(1) and K(1) and then adds it to L(0) and K(0)"""
def dot(L,K):
    if L == [] or K == []:
        return 0
    else:
        return (mult(L[0],K[0])) + dot(L[1:],K[1:])
    x
print(dot([5,3], [6,4]))
"""Using recursion you can make the program go through the entire string and turn it into a list"""
def explode(s):
    if s== "":
        return []
    return [s[0]] + explode(s[1:])
    
    
print(explode('hello'))
"""The ind function goes through a list and locates where the desired number is. Using if statements and recursion it goes through the entire list"""
def ind(e,L):
    if L == [] or L=='':
        return 0
    if e == L[0]:
        return 0
    return ind(e,L[1:])+1
    """removeAll uses recursion to go through a list and remove the deseired tagret value and then prints the list"""
def removeAll(e, L):
    if L== []:
        return []
    if e == L[0]:
        return removeAll(e,L[1:])
    return [L[0]]+ removeAll(e,L[1:] )

"""Filter runs through  a list and prints it"""
def myFilter(f, L):
    if L == []:
        return []
    if f(L[0]) == True:
        return [L[0]]+ myFilter(f,L[1:])
    return myFilter(f,L[1:])
"""Using recursion it reverses the order of lists inside of lists"""
def deepReverse(L):
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    
"""I pledge my honor that I have abided by the Stevens Honor system - BRandon Soong"""
     


 

    
    

    
    
    

    
    
    
  


    
    
    
    
            
    
        


    

    