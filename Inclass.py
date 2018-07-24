'''
Created on Nov 27, 2017

@author: brand
'''
def numberfinder():
    sum = 0 
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(numberfinder())

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib():
    L = ['www', 'stevens', 'edu', 'sit', 'registrar']
    M = range( len(L), -1, -2 ) 
    print(L[M[2]])