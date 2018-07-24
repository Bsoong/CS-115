'''
Created on Oct 18, 2017

@author: brand
'''
from test.test_largefile import size
COMPRESSED_BLOCK_SIZE = 5
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE -1

def countRun(s, c, maxRun):
    """
    param s: a string
    param c: what we are counting
    maxRun: maximum length of runtime
    Returns the number of times that string occurs in a row
    """
    if s =="":
        return 0
    if s[:len(c)] != c:
        return 0
    return 1 + countRun(s[1:], len(c), maxRun)

    
    
    

def compress(s):
    """
    param s: string to compress
    count the runs in s switching from counting runs of zeros to countring runs of ones
    Return a compressed string.
    """
    def helper(s,c):
        if s == "":
            return []
        runLen = countRun(s, c, MAX_RUN_LENGTH)
        return [runLen] + helper(s[runLen:], '0' if c == '1' else '1')
    return helper(s, '0')

def uncompress(s):
    """
    param s:
    in chunks of COMPRESSED_BLOCK_SIZE,
    convert the binary representation of a number
    in that block into that many zeros or ones,
    switching from decompressign zros to decompressive
    ones alternatively.
    Returns a decompressed string
    """
    def helper(s,c):
        first = s[:COMPRESSED_BLOCK_SIZE]
        temp = something(first)
        return temp + helper(s[COMPRESSED_BLOCK_SIZE:], nextC)
    
def compression(s):
    """
    Divide compressed size by original size
    """