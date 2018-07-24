'''
Created on Sep 25, 2017

@author: brand
'''
def confuse(s):   
    if len(s) <= 1: 
        return s    
    x = len(s) // 2  
    return confuse(s[:x]) + confuse(s[x:])

print(confuse('annoy'))