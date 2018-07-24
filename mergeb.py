'''
Created on Nov 9, 2017

@author: brand
'''

def num_matches(list1, list2):
    '''returns the number of elements that the two lists have in common'''
    list1.sort()
    list2.sort()
    end_line = []
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches +=1
            i +=1
            j+=1
        elif list1[i] < list2[j]:
            i+=1
        else:
            j+=1
    return matches
    
def keep_matches(list1,list2):
    '''Returns a list of the elements that the two lists have in common'''
    list1.sort()
    list2.sort()
    end_line = []
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            end_line.append(list1[i])
            matches +=1
            i +=1
            j+=1
        elif list1[i] < list2[j]:
            i+=1
        else:
            j+=1
    return end_line
    
def drop_matches(list1, list2):
    list1.sort()
    list2.sort()
    end_line = []
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches +=1
            i +=1
            j+=1
        elif list1[i] < list2[j]:
            end_line.append(list1[i])
            i+=1
        else:
            end_line.append(list2[j])
            j+=1
    while i < len(list1):
        end_line.append(list1[i])
        i+=1 
    while j<len(list2):
        end_line.append(list2[j])
        j+=1
    return end_line
    
print(num_matches(['b','d','e'], ['a', 'b' ,'c', 'd']))
print(keep_matches(['b','d','e'], ['a', 'b' ,'c', 'd']))
print(drop_matches(['b','d','e'], ['a', 'b' ,'c', 'd']))