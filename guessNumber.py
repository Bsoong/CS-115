'''
Created on Nov 2, 2017

@author: brand
'''
import random

MAX_TRIES = 7
print('''---Welcome to Guess my Number---

I\'m thinking of a number between 1 and 100.
Try to guess the number in %d''' %MAX_TRIES, end='')

if MAX_TRIES == 1:
    print(' attempt...')
else: 
    print(" attempts...")

#set the initial Values
number = random.randint(1,100)
tries = 1
guess = int(input("Enter guess %d: " % tries))

#Guessing Loop
while guess != number:
    if guess > number:
        print('    Lower...')
    else: 
        print('    Higher...')
    tries += 1
    if tries > MAX_TRIES:
        break
    guess = int(input("Enter guess %d: " % tries))

if tries <= MAX_TRIES:
    print("\nCongratulations! You correctly guessed the numbed %d, and it only took you %d" % (number, tries), end='')
    if tries== 1:
        print(' try!')
    else:
        print(' tries!')
else:
    print('\nSorry, you did not guess the number %d in %d' % (number, MAX_TRIES))
if tries== 1:
     print(' try!')
else:
    print(' tries!')