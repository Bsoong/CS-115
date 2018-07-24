'''
Created on Oct 3, 2017

@author: brand
'''
"""
Memoization
1. If the key is in the memo, return the value associated with the Key
2. DO work! Use recursion to compute your answer, but store the result in a local variable.
3. Put the Result in the memo and return the result
{} == Dictionary brackets
"""
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
    
def fib_memo(n):
    def fib_helper(n,memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n-1, memo)+fib_helper(n-2, memo)
        memo[n] = result
        return result
    return fib_helper(n, {})
def LCS(s1,s2):
    """Returns the length of the longest common subsequence in strings s1 and s2."""
    if s1 == '' or s2 == '':
        return 0
    elif s1[0]==s2[0]:
        return 1 + LCS(s1[1:],s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))

def LCS_memo(s1,s2):
    def LCS_helper(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1,s2)]
        if s1 == '' or s2 == '':
            return 0
        elif s1[0] == s2[0]:
            result = 1 + LCS_helper(s1[1:], s2[1:], memo)
        else:
            result = max(LCS(s1, s2[1:]), LCS(s1[1:], s2)) , LCS_helper(s1[1:],s2,memo)
        memo[(s1,s2)] = result
        return result
    return LCS_helper(s1,s2,{})
print(fib_memo(90))