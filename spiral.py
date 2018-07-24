'''
Created on Oct 5, 2017

@author: brand
'''

import turtle

"""Distance  - Length of current wall 
initial -- length of the first wall on the inner part of the spiral"""
def square_spiral(walls):
    def square_spiral_helper(distance, initial, count ):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(distance + initial *(count%2) , initial, count+1)
            
        
def octag(walls):
    def octag_helper(distance, initial, count ):
        if count == walls:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            octag_helper(distance + initial *(count%2) , initial, count+1)        
    octag_helper(20, 5, 0)
    
octag(30)
square_spiral(30)