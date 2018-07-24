'''
Created on Oct 31, 2017

@author: brand
'''

def mapSqr(L):
    result = []
    for x in L:
        result.append(x*x)
    return result


def max_finder(L):
    if L == 0:
        return None
    maxval = L[0]
    for x in L:
        if  x > maxval:
            maxval =x
    return maxval

def find_min_max(lst):
    if lst == []:
        return 0
    maximum = minimum = lst[0]
    for x in lst:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    return minimum,maximum

def sequential_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1
def shallow_copy(L):
    x = []
    for y in L:
        x.append(y)
    return x
L =[1,2,3]
M = shallow_copy(L)
M[2] = 33


def deep_copy(L):
    new_list = []
    for x in L:
        if isinstance(x, list):
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list
    

S = [[1,2], [3,4], [5,6]]
T = deep_copy(S)
T[2][1] = 66

def create_board(r, c):
    board = []
    for i in range(r):
        row=[]
        for _ in range(c):
            row.append(' ')
        board.append(row)
    return board
def create_board_comp(r, c):
     return [ [' ' for _ in range(c)] for _ in range(r)  ]
   
board = create_board(3, 3)

def display_board(board):
    num_rows = len(board)
    for row in range(num_rows):
        num_cols = len(board[row])
        for col in range(num_cols):
            print(' ' + board[row][col] + ' ', end = '')
            if col < num_cols - 1:
                print('|', end = '')
        print()
        if row < num_rows-1:
            print('-' * (num_cols * 4-1))

def find_max_2d(L):
    max_val = L[0][0]
    for row in L:
        for x in row:
            if x > max_val:
                max_val = x
    return max_val
            
def find_max_coords_2D(L):
    max_coords = L[0][0]
    row = col = 0 
    for r in range(len(L)):
        for c in range(range(l[r])):
            if L[r][c] > max_coords:
                max_coords = L[r][c]
                row = r
                col = c
    return row, col
        
def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    
def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_index  = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i , min_index)
    
            
print(mapSqr([2,3,4,5,6]))
print(max_finder([1,2,3,4,5,6]))
print(find_min_max([1,3,4,5,6,7]))
print(sequential_search([1,2,3,4,5,6,7,8,9], 5))
print(L)
print(M)
print(S)
print(board)
board = create_board_comp(3, 3)
board[0][0] = 'X'
board[2][2] = 'O'
print(board)
display_board(board)