'''
Created on Nov 2, 2017

@author: brand
'''
import  cs5png import *

def mult(c, n):
    """Uses a for loop to add c to the amount of value n"""
    result =0
    for _ in range(n):
        result += c
    return result

def update(c, n):
    """updates the variable z to the formula z**2+c"""
    z = 0
    for _ in range(n):
        z = z**2 +c
    return z

def inMset(c, n):
    """uses the update function, but rather then returning z,it returns boolean"""
    z = 0
    for _ in range(n):
        z = z**2 +c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel( col, row ):
 """ a function that returns True if we want
 the pixel at col, row and False otherwise
 """
 if col%10 == 0 and row%10 == 0:
 return True
 else:
 return False
def test():
 """ a function to demonstrate how
 to create and save a png image
 """
 width = 300
 height = 200
 image = PNGImage(width, height)
 # create a loop in order to draw some pixels

 for col in range(width):
 for row in range(height):
 if weWantThisPixel( col, row ) == True:
 image.plotPoint(col, row)
 # we looped through every image pixel; we now write the file
 image.saveFile()