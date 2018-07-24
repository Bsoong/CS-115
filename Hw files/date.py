'''
Created on _______________________
@author:   Brandon Soong
Pledge:    I pledge my Honor that I have abided by the Stevens Honor System -bsoong

CS115 - Hw 11 - Date class
'''

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
         as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
    
    def tomorrow(self):
        """adds a day and returns the proper date"""
        DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if self.month == 12 and self.day == 31:
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.month == 2 and self.day == 28 and self.isLeapYear():
            self.month = 2 
            self.day += 1
        elif self.day == 31:
            self.month += 1
            self.day = 1
        elif self.day >= DAYS_IN_MONTH[self.month]:
            self.month += 1
            self.day = 1
        else: 
            self.day += 1
    def yesterday(self):
        """Subtracts a day and returns the proper date"""
        if self.month == 1 and self.day == 1:
            self.month = 12
            self.day = 31
            self.year -= 1
        elif self.month == 3 and self.day == 1 and self.isLeapYear():
            self.month = 2 
            self.day = 29
        elif self.day == 1:
            self.day = DAYS_IN_MONTH[self.month -1]
            self.month -=1 
        else: 
            self.day -= 1
    def addNDays(self, N):
        """adds a day and prints the dates"""
        for _ in range(N):
            print(self)
            self.tomorrow()
        print(self)
            
    def subNDays(self, N):
        """subtracts a day and prints the dates"""
        for _ in range(N):
            print(self)
            self.yesterday()
        print(self)
    def isBefore(self, d2):
        """Determines whether a date is before or after the other, and then returns a boolean"""
        if self.equals(d2):
            return False
        if self.year  < d2.year:
            return True
        if self.year == d2.year:
            if self.month < d2.month:
                return True
        if self.year == d2.year:
            if self.month == d2.month:
                if self.day < d2.day:
                    return True
        else:
            return False

    def isAfter(self, d2):
        """FInds out if a date is before or after each other and returns a boolean"""
        if self.equals(d2):
            return False
        if self.isBefore(d2) == True:
            return False
        else: 
            return True
    def diff(self, d2):
        """Finds the difference in days between self and d2"""
        x=0
        y = self.copy()
        while y.isBefore(d2) == True:
            y.tomorrow()
            x-=1
        if x != 0:
            return x
        
        while y.isAfter(d2) == True:
            y.yesterday()
            x+=1
        return x
    def dow(self):
        """Finds the day of the week and prints a string"""
        know = Date(11,9, 2011)
        dict = {0 : 'Wednesday' , 1 : 'Thursday' , 2 : 'Friday' , 3 : 'Saturday' , 4 : 'Sunday' , 5 : 'Monday' , 6 : 'Tuesday'}
        x = self.diff(know)
        return dict[x % 7]
        
if __name__ == '__main__':
    d = Date(10,28,1929)
    print(d.dow())
    print(d)
    



        
        
