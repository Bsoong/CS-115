'''
Created on 10/12
@author:   Brandon Soong
Pledge:   I pledge my Honor that I have abided by the Stevens Honor System-Bsoong

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2 == 1:
        return True
    return False
print(isOdd(5))

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n) == True:
        return numToBinary(n//2)+"1"
    return numToBinary(n//2)+"0"
print(numToBinary(156))
        
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def helper(s, ex):
        if s == '':
            return 0
        return helper(s[:-1], ex+1) + int(s[-1]) * (2**ex)
    return helper(s, 0)

print(binaryToNum('10011100'))
        
        


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return "00000000"
    return ('0' * (8 - len(numToBinary(binaryToNum(s)+1)))) + numToBinary(binaryToNum(s)+1)


print(increment("00000001"))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else: 
        print(s)
        return count(increment(s),n-1)


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
       return ''
    return numToTernary(n//3) + str(n%3)

    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def helper(s, ex):
        if s == '':
            return 0
        return helper(s[:-1], ex+1) + int(s[-1]) * (3**ex)
    return helper(s, 0)



