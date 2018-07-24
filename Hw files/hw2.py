'''
Created on _______________________
@author:   Brandon Soong & Anthony Ciccone
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - Bsoong Aciccone

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
#bestCode
#pointsList
#codePoints
#numberPoints
#list_of_codes_created
#is_code_possible
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
    [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    """Returns the points for a given number"""
    if scorelist == []:
        return 0 
    first = scorelist[0]
    if first[0]== letter:
        return first[1]
    return letterScore(letter, scorelist[1:])

def codePoints(code, pointslist):
    """Code points adds the values of the numbers of the entire length of the word """
    if code == '':
        return 0 
    return letterScore(code[0], pointslist) + codePoints(code[1:], pointslist)

def wordScore(S, scorelist):
    """Prints the word value according to scorelist"""
    if S == '':
        return 0 
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def is_code_possible(code, numbers):
    """Checks to see if the code is possible and returns a boolean"""
    if code == '':
        return True
    if code[0] in numbers:
        return is_code_possible(code[1:], remove(code[0], numbers))
    else:
        return False

def remove(number,numbers):
    """Remove function uses recursion to remove a value at a specific value"""
    if numbers == []:
        return [] 
    if number == numbers[0]:
        return numbers[1:]
    else:
        return [numbers[0]] + remove(number, numbers[1:])

def list_of_codes_created(dictionary, numbers):
    """Runs through the string of words using the filter, and puts the words into a list"""
    return filter(lambda code: is_code_possible(code, numbers),dictionary)

def scoreList(rack):
    """Scorelist creates combinations of the words in the list based on the dictionary and returns the word and value"""
    codes = list_of_codes_created(Dictionary, rack)
    return map( lambda code: [code, codePoints(code, scrabbleScores) ],codes)

def bestWord(rack):
    """ bestWord uses the rack given and makes the comparison with lambda to decide what the bestoWord is"""
    contenders = scoreList(rack) 
    return reduce(lambda x, y: x if x[1] > y[1] else y, contenders, ['',0])
    

print(letterScore('c', scrabbleScores))
print(scrabbleScores[0][1])
print(wordScore('Mommy', scrabbleScores))
print(scoreList(['a', 's', 'm', 't', 'p']))
print(bestWord(['g', 'y', 'e']))