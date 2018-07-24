'''
Created on Sep 10, 2017

@author: brand
'''
from   cs115 import map, reduce

def mult(x,y):
    return x*y

def factorial(n):
    """Using an if and an else statement, it allows for the function to hit all parameters or any 
    number that may be put in. The if makes sure the statement is possible and the the else multiplies
    by itself to create the value of n!"""
    return reduce(mult, range(1,n+1))

def add(a,b):
    """Simple add function to add two numbers together"""
    return a+b

def mean(x):
    """Mean is the sum of the numbers/the amount, so using reduce and the add function youre able to add
    x value and then divide it by the list"""
    list= len(x)
    return ((reduce(add, x)/list))
list=[]
def prime(n):
    if n==1:
        return True
    return factorial(n-1)%n==n-1
    
       
    
print(prime(1))        
    






    
    