'''
Created on Sep 18, 2017

@author: brand
'''
from cs115 import map, reduce
def powerset(lst):
    """returns the powerset of the list that is, the set of all subsets of the list."""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]]+ subset, lose_it)
    return lose_it + use_it

print(powerset(['a', 'b', 'c']))
"""'and' and 'or' are shortcircuit operators in Python. The second operand is not evaluated when the overall result can be deduced sikmply by evaluating the first operand"""
def subset(target, lst):
    """Determines wherher or not it is possible to create target sun using the values in the list can be positive, negative or zero."""
    if target == 0:
        return True
    if lst == []:
        return False
    use_it = subset(target - lst[0], lst[1:])
    lose_it = subset(target, lst[1:])
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

print(subset(8, [1,2,3,4,5,7,8,6,5]))

def subset_with_values(target, lst):
    """Determines wgether or not it is possible to create the target sum using values in the list. Values in the list can be positive, negative, or zero. 
    The functionn returns a tuple of exactly two items. The first is a Boolean that indicates true if sum is possible and False if its not.
     The second element in the tuple is a list of all values that add up to the target sum"""        
    if target == 0 :
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return(True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

print(subset_with_values(8, [5,8,2,2]))
            
def LCS(s1,s2):
    """Returns the length of the longest common subsequence in strings s1 and s2."""
    if s1 == '' or s2 == '':
        return 0
    elif s1[0]==s2[0]:
        return 1 + LCS(s1[1:],s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))

print(LCS('top', 'bot'))

def LCS_with_values(s1, s2):
    if s1 == '' or s2 == '':
        return (0,[])
    elif s1[0] ==s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return(1 + result[0],s1[0] + result[1])
    uses1 = LCS_with_values(s1, s2[1:])
    uses2 = LCS_with_values(s1[1:], s2)
    if uses1[0] > uses2[0]:
        return uses1
    return uses2
        
def coin_row(lst):
    return 0 if lst == [] else max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]) )

def coin_row_with_values(lst):
    if lst == []:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it 

print(coin_row([5, 1, 2, 10, 6, 2]))

def distance(first, second):
    if first == '':
        return len(second)
    if second == '' : 
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:] , second[1:])
    substitution = distance(first[1:] , second[1:])
    deletion = distance(first[1:], second)
    insertion = distance(first , second[1:])
    return 1 + min(substitution, deletion, insertion)
print(distance('sally' , 'bally'))

