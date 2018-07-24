'''
Created on Sep 12, 2017

@author: brand
'''
from cs115 import map, reduce
import math
def tower(n):
    """computes 2^(2^2...) with n twos, using recursion"""
    if n==0:
        return 1
    return 2 ** tower(n-1)

print(map(tower,range(5)))

def tower_reduce(n):
    def power(x,y):
        return y ** x
    if n == 0:
        return 1
    return reduce(power, [2] *n)

print(map(tower_reduce, range(5)))

def len(lst):
    """Returns the length of the lst"""
    if len(lst) == []:
        return []
    else:
        return 1 + len(lst[1:])
    
def reverse(lst):
    """takes and input a list of elements and returns the list in reverse order"""
    if lst == []:
        return 0
    else:
        return reverse(lst[1:]) + lst[0]
    
def member(x,lst):
    """Returns True if X is contained in the list and False Otherwise"""
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return False
         
print(reverse([1,2,3,4]))

def power(x,y):
    if x==0:
        return 1
    return x*power(x,y-1)

def power_tail(x,y):
    def power_tail_helper(x,y,accum):
        if y==0:
            return accum
        return power_tail_helper(x,y-1,x*y)
    return power_tail_helper(x,y,1)

def my_map(f,lst):
    if lst== []:
        return []
    return my_map(f,lst[1:]) + my_map(f,lst[1:])
def my_reduce(f, lst):
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:],f(lst[0], accum))
    if lst== []:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])
def prime(n):
    """Returns whether or not an integer is prime."""
    possible_divisors = range(2, int(math.sqrt(n))+1)
    divisors= filter(lambda x: n%x == 0, possible_divisors)
    return len(divisors) == 0 
def primes(n):
    def sieve(lst):
        """Returns a list of primes in the range [2,n] computed via the seve of Eratosthenes"""
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x%lst[0] !=0, lst[1]))
    return sieve(range(2,n+1))

def fib(n):
    """Tree recursion-- occurs when the pending operation for the recursive call is another recursive call"""
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
    
print(fib(3))    