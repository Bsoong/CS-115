'''
Created on Sep 5, 2017

@author: brand
'''

def fahrenheit(celsius): 
    """Returns the input Celsius degrees in Fahrenheit."""
    return 9 / 5 * celsius + 32
    
def celsius(fahrenheit):
        """Returns the input Farenheit degrees in Celsius."""
        return 5 / 9 * (fahrenheit-32)

"""Call the Functions Below the FUnctions deffinitions"""
c = float(input('Enter degrees in Celsius: '))
f=fahrenheit(c)
#You can print multiple items in one statement if you put a comma after each item. it prints a space and then goes on to print the next item
print(c,'C =', f, 'F')
#You can print this way too, but allowing exactly two decimal places
print('%.2f C = %.2f F' % (c,f))

f = float(input('Enter degrees in Fahrenheit: '))
c = celsius(f)
print(f, 'F =', c, 'C')
print()
f=float(input('Enter Degrees in Fahrenheit:'))
#Use assert to check the return value is equal to the expected Value
assert fahrenheit(celsius(f)) == f
