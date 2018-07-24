#
# life.py - Game of Life lab
#
# Name:Brandon Soong
# Pledge: I pledge my Honor that I have abided by the Stevens Honor System -Bsoong
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for _ in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''returns a 2d array with "height" rows and "width" cols'''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A



def printBoard(A):
    """This function prints the 2d list-of-lists A without spaces (using sys.stdout.write"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col))
        sys.stdout.write( '\n') 
        
def diagonalize(width,height):
    """ creates an empty board and then modifies it
     so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


def innerCells(width, height):
    """makes all of the inside 0's into 1's"""
    A = createBoard(width, height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = 1
    return A
            

def randomCells(width, height):
    """creates a random array of 1's and 0's with the outside row/columns being 0"""
    A = createBoard(width, height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = random.choice([0,1])
    return A


def copy(A):
    """Deep copy makes an identical copy that can be altered by the original"""
    new_list = []
    for x in A:
        if isinstance(x, list):
            new_list.append(copy(x))
        else:
            new_list.append(x)
    return new_list

def innerReverse(A):
    """Swaps the 1's in one list, and then changes it to a 0. If it is a 0 then it switches to a 1.""" 
    newA = copy(A)
    width = len(A)
    height = len(A[0])
    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA 


def countNeighbors( row, col, A):
    """counts the number of 'neighbors' around a specific row and column"""
    count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if A[r][c] == 1:
                count += 1
    if A[row][col] == 1:
        count -= 1
    return count        
                
def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    newA = copy(A)
    width = len(A)
    height = len(A[0])
    for row in range(1, height-1):
        for col in range(1, width-1):
            if countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
            elif countNeighbors(row, col, A) < 2 or countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
    return newA





    
