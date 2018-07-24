'''
Created on Oct 3, 2017

@author: brand
I pledge my honor that I have abided by the Stevens Honor System -Bsoong
'''

def pascal_row(x):    
    """Uses Pascal Helper to return the return 1 --> added function <-- 1"""
    def pascal_helper(lst):
        """Pascal helper creates the real list  that is used for row."""
        if lst == []:
            return []
        if len(lst) == 1:
            return [lst[0]]
        if len(lst) == 2:
            return [lst[0]+lst[1]]
        else:
            return [lst[0]+lst[1]]+pascal_helper(lst[1:])
    if x == 0:
        return [1]
    if x == 1:
        return [1,1]
    else:
        return [1]+pascal_helper(pascal_row(x-1)) + [1]
    
def pascal_triangle(x):
    """Adds the pascal_row function into a list"""
    if x == 0:
        return [[1]]
    return pascal_triangle(x-1) + [pascal_row(x)]


print(pascal_triangle(0))
print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))

