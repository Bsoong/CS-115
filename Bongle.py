'''
Created on Sep 18, 2017

@author: brand
'''
[0,9,8]
Dictionary = ['902', '820', '888','270', '999', '123', '456', '789', '209', '884', '423', '723', '210']

bonglepoints = []


def numberPoints(number, pointslist):
    """Returns the points for a given number"""
    if pointslist == []:
        return 0.0 
    first = pointslist[0]
    if first[1]== number:
        return first[1]
    return numberPoints(number, pointslist[1:])
    
def codePoints(code, pointslist):
    if pointslist == '':
        return 1 
    return numberPoints(code[0], pointslist) * codePoints(code[1:], pointslist)
    
    
def list_of_codes_created(dictionary, numbers):
    return filter(lambda code: is_code_possible(code, numbers),dictionary)
    
def is_code_possible(code, numbers):
    if code == '':
        return True
    if code[0] in numbers:
        return is_code_possible(code[1:], remove(code[0], numbers))
    else:
        return False
    
def remove(number,numbers):
    if numbers == []:
        return [] 
    if number == numbers[0]:
        return numbers[1:]
    else:
        return [numbers[0]] + remove(number, numbers[1:])
    
def pointsList(numbers):
    codes = list_of_codes_created(Dictionary, numbers)
    return map( lambda code: [code, codePoints(code, bonglepoints) ],codes)

def bestCode(numbers):
    contenders = pointsList(numbers) 
    def better_coder(x,y):
        if x[1] > y[1]:
            return x
        return y
        return reduce(lambda x, y: x if x[1] > y[1] else, contenders)



    
    
print(remove('9', ['0', '9', '8']))
print(is_code_possible('910', ['0','9','8']))
    

        