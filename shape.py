'''
Created on Nov 21, 2017

@author: brand
'''
from abc import *

class Shape(metaclass = ABCMeta):
    def __init__(self, x, y, name = 'Shape'):
        self.__x = x
        self.__y = y
        self.__name = name
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    @x.setter
    def x(self, x):
        self.__x = x
        
    @y.setter
    def y(self, y):
        self.__y = y
    def area(self):
        pass
    def __str__(self):
        return self.__name + ' at (' + str(self.__x) + ',' + \
            str(self.__y) + ')'
if __name__ == '__main__':
    try: 
        a = Shape(10,20)
    except TypeError as Error:
        print('Error', Error)