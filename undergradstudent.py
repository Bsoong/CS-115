'''
Created on Nov 20, 2017

@author: brand
'''
from student import Student
from http.cookies import _warn_deprecated_setter

class UndergradStudent(Student):
    def  __init__(self, first_name, last_name, sid, gpa, meal_plan_balance):
        super().__init__(first_name, last_name, sid, gpa)
        self.__meal_plan_balance = meal_plan_balance
    def __str__(self):
        return super().__str__() + ', Meal Plan Balance: $' \
            +str(self.__meal_plan_balance)    
    @property
    def meal_plan_balance(self):
        return self.__meal_plan_balance
    @meal_plan_balance.setter
    def meal_plan_balance(self, meal_plan_balance):
        self.__meal_plan_balance = meal_plan_balance
    
print(__name__)
if __name__ == '__main__':
    u1 = UndergradStudent('John', 'Doe', '123456', 1.6, 1000)
    print(u1)