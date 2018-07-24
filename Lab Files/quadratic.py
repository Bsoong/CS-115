'''
Created on Nov 16, 2017

@author: brand
I pledge my honor that I have abided by the Stevens Honor System- Bsoong
'''
import math
class QuadraticEquation(object):
    
    def __init__(self, a, b, c):
        """Method Constructor that sets the values for A and accounts for the case that would break the code"""
        if a == 0: 
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        else:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)
            
    @property
    def a(self):
        """Attribute that changes self.__a"""
        return self.__a
    
    @property
    def b(self):
        """Attribute that changes self.__b"""
        return self.__b
    
    @property
    def c(self):
        """Attribute that changes self.__c"""
        return self.__c
    
    def discriminant(self):
        """Method that uses functions above to change the calculate the b^2-4ac"""
        return self.__b**2 - (4 * self.__a * self.__c)
    
    def root1(self):
        """Running the positive version of the Quadratic equation"""
        if self.discriminant() < 0.0:
            return None
        return(-self.__b + math.sqrt(self.discriminant()))/(2*self.__a)
        
    
    def root2(self):
        """Running the negative version of the Quadratic Equation"""
        if self.discriminant() < 0.0:
            return None
        return(-self.__b - math.sqrt(self.discriminant()))/(2*self.__a)
    
    def __str__(self):
        a1 = str(self.__a) + 'x^2 '
        b1 = '+ ' + str(self.__b) + 'x '
        c1 = ' + ' + str(self.__c)
        if self.__a == 1:
            a1 = 'x^2 '
        if self.__a == -1:
            a1 = '-x^2 '
        if self.__a <-1:
            a1 = '-' + str(self.__a *-1) + 'x^2 '
            
        if self.__b == 1:
            b1 = '+ x'
        if self.__b == -1:
            b1 = '- x'
        if self.__b <-1:
            b1 = '- ' + str(self.__b *-1) + 'x '
        if self.__b == 0:
            b1 = ''
        
        if self.__c == 0:
            c1 =  ''
        if self.__c < -1:
            c1 = '- ' + str(self.__c*-1)
        final = a1 + b1 + c1 + ' = 0'
        return final.replace('  ',' ' )
        

        
        
        
    
        
        
       
            
            
    
    
