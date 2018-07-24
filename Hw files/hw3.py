'''
Created on _______________________
@author:   Brandon Soong
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. -Bsoong

CS115 - Hw 3
'''
from cs115 import map, reduce, filter
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def giveChange(amount, coins):
    """Give change takes in an amount, and then prints the list of coins used to create the amount. This is done
    through the use of use_it and Lose_it functions"""
    if amount == 0:
        return [0 , []]
    if coins == []:
        return [float("inf"), []]
    if coins[0] > amount:
        return [float("inf") , []]
    use_it = giveChange(amount - coins[0], coins)
    lose_it = giveChange(amount, coins[1:])
    numOfCoins = min(1+use_it[0], lose_it[0])
    if 1+use_it[0] < lose_it[0]:
        return [numOfCoins, use_it[1] + [coins[0]]]
    return [numOfCoins, lose_it[1]]
        
print(giveChange(48, [1, 5, 10, 25, 50]))


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores): 
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scorelist):
        """taken fron Hw2, Letter score returns the letter and score from a specific spot in a list."""
        first = scorelist[0]
        if first[0]== letter:
            return first[1]
        return letterScore(letter, scorelist[1:])
    def wordScore(S):
        """With some slight alterations from hw2, Wordscore now only takes one input of S, and then calls
        letterScore, within the function, and then finally maps the function and dct."""
        if S == '':
            return ['', 0]
        return [S ,letterScore(S[0], scores) + wordScore(S[1:])[1]]
    return map(wordScore, dct)

print(wordsWithScore(Dictionary, scrabbleScores))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0: 
        return []
    return [L[0]] + take(n -1 , L[1:]) 

print(take(5, [1,2,3,4,5,6]))




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0: 
        return L
    return drop(n -1 , L[1:]) 

print(drop( 3 , [1,2,3,4,5]))


