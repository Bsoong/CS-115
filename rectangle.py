'''
Created on Nov 21, 2017

@author: brand
'''
from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, length, width, name = 'Rectangle'):
        super().__init__(x, y, name)
        self.__length = length 
        self.__width = width
        
    @property
    def length(self):
        return self.__legnth
    def width(self):
        return self.__width
    @length.setter
    def length(self, length):
        self.__length = length
        
    @width.setter
    def width(self, width):
        self.__width = width
    @property
    def area(self):
        return self.__length * self.__width
    def __str__(self):
        return super().__str__() + ', length = ' + \
        str(self.__length) + ', width = ' + str(self.__width) + \
        ', area = ' + str(self.area)
if __name__ == '__main__':
    rect = Rectangle(10, 10 ,20, 20)
    print(rect)
    rect.x = 30
    rect.y = 35
    print(rect)