'''
Created on Sep 21, 2017

@author: brand

I pledge my Honor that I have abided by the Stevens Honor System. -- Bsoong

'''
def change(amount, coins):
    """By using if statements ,you create base cases for the recursion of the function change. Once done, you run through
    the first term in the list coins, and if it the amount is less than the firsttest, then it does recursion without the first term to get all
    of the values needed. If none of the statements are needed then it finally returns the min value of the use_it and lose_it functions"""
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    else:
        firsttest = coins[0]
        if firsttest > amount:
            return change(amount, coins[1:])
        else:
            use_it = 1+change(amount - firsttest, coins)
            lose_it = change(amount,coins[1:])
            return min(use_it,lose_it)
        

        
        
        
    
