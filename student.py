'''
Created on Nov 13, 2017

@author: brand
'''
import sys
from test.test_heapq import SideEffectLT
"""
A class is a blueprint for an object. Classes contain properties(Often called attributes or fields) and methods (functions) that change the 
state of the object. We'll start with a special method called the constructor, whose purpose is to initialize the fields of the objects. 
When you invoke the constructor and creat an object value, you have performed instantiation.
"""

class Student(object):
    def __init__(self, first_name,last_name, sid, gpa):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sid = sid
        self.__gpa = float(gpa)
        
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
        
    @property
    def sid(self):
        return self.__sid
    
    @sid.setter
    def sid(self, sid):
        self.__sid = sid
    
    @property
    def gpa(self):
        return self.__gpa
    
    @property
    def gpa(self, gpa):
        self.__gpa = gpa
        
    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ' (SID:' +  \
            self.__sid + ', GPA ' + str(self.__gpa) + ')'
    @gpa.setter
    def gpa(self, gpa):
        try:
            local_gpa = float(gpa)
        except:
            raise TypeError('GPA must be a float.')
        if local_gpa < 0.0 or local_gpa >4.0:
            raise ValueError('GPA must be between 0.0 and 4.0')
        self.__gpa = local_gpa
        
if __name__ == '__main__':
    s = Student('Jeremy', 'Doll', '55555555', '1.8')
    print(s)
    print(s.first_name)
    s.first_name = "Brian"
    try:
        s.gpa = input('Enter new GPA: ').strip()
    except (TypeError, ValueError) as error:
        print ('Error: ', error)
        sys.exit(1)
    print(s)

"""
Normally, we have getters(accessors) and setters(mutators) for reading and modifying the value of the fields. @property
"""