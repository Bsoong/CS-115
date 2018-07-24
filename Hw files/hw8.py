'''
Created on Oct 31, 2017

@author: brand
I pledge my honor that I have abided by the Stevens Honor system.-Bsoong

'''
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    if s[-1]== '0':
        return 2*binaryToNum(s[:-1])
    return (binaryToNum(s[:-1]))*2 +1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n%2 == 0:
        return numToBinary(n/2)+"0"
    return numToBinary((n-1)/2)+"1"
def swap(s):
    """Swap function that changes 1 to 0's and 0's to 1's"""
    if s== '':
        return ''
    if s[0] == '1':
        return '0'+ swap(s[1:])
    return '1' + swap(s[1:])
def TcToNum(s):
    """Converts from two's complement to a number using fucntions made in previous labs"""
    if s[0] == '1':
        return -(binaryToNum(swap(s))+1)
    return binaryToNum(s)
def lengthfixer(s):
    """previous function that makes sure that the length of the string actually equals 8"""
    if len(s)==8:
        return s
    return lengthfixer('0'+s)
def NumToTc(n):
    """Using the previous functions, and one lengthy return, Num to TC converts the number into TC"""
    if n > 127 or n <-128:
        return 'Error'
    if n < 0:
        return numToBinary(binaryToNum(swap(lengthfixer(numToBinary(-n))))+1)
    return lengthfixer(numToBinary(n))

    
     