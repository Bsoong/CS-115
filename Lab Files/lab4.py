'''
Created on Sep 28, 2017

@author: brand
I pledge my honor that I have abided by the Stevens Honor System  - Bsoong
'''


def knapsack(capacity, itemList):
    """Runs through a list  of items, and returns a tuple and pulls out the most valuable items in the list, so long as the capacity provides"""

    if itemList == []:
        return [0,[]]
    if capacity <= 0:
        return [0,[]]
    if capacity < itemList[0][0]:
        return knapsack(capacity,itemList[1:])
    use_it = knapsack(capacity - itemList[0][0], itemList[1:])
    use2 = [use_it[0] + itemList[0][1], [itemList[0]] + use_it[1]]
    lose_it = knapsack(capacity, itemList[1:])
    lose2 = [lose_it[0], lose_it[1]]
    if use2 > lose2:
        return use2
    return lose2
                             
