'''
Created on 10/11
@author:   Brandon Soong
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. - Bsoong

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    """sv_tree uses a helper function so that the Turtle syntax works properly"""
    def sv_tree_helper(trunk_length, levels):
        """By calling the function, it recursively runs through each part of the tree 
        constantly decreasing the the length and the amt of angles."""
        if levels == 0:
            return 
        else:
            turtle.forward(trunk_length)
            turtle.left(45)
            sv_tree_helper(trunk_length/2 , levels-1)
            turtle.right(90)
            sv_tree_helper(trunk_length/2, levels-1)
            turtle.left(45)
            turtle.backward(trunk_length)
            return
            
            
            
        
        #return sv_tree_helper(trunk_length/2, levels-1)
            
            
    sv_tree_helper(trunk_length, levels)
    turtle.done()
 # TODO

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fast_lucas_helper(n, memo):
        """Fast lucas helper is similar to fibonacci memoization with small alterations"""
        if n in memo:
            return memo[n]
        if n == 0:
            return 2
        if n == 1:
            return 1
        else:
            result = fast_lucas_helper(n-1, memo)+fast_lucas_helper(n-2, memo)
        memo[n] = result
        return result
    return fast_lucas_helper(n, {})
    
        
        

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        """Fast change takes the original change function and memoizes it"""
        if amount in memo:
            return memo[amount]
        elif amount == 0:
            result = 0
        elif coins == ():
           result = float("inf")
        else:
            firsttest = coins[0]
            if firsttest > amount:
                result = fast_change_helper(amount, coins[1:], memo)
            else:
                use_it = 1+fast_change_helper(amount - firsttest, coins, memo)
                lose_it = fast_change_helper(amount,coins[1:], memo)
                result = min(use_it,lose_it)
        memo[amount] = result
        return result
    return fast_change_helper(amount, tuple(coins), {})
  

        

    # Call the helper. Note we converted the list to a tuple.
    #return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
