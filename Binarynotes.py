'''
Created on Oct 10, 2017

@author: brand
'''
"""To convert Decimal to binary, repeatedly divide the number by two and take the remainder. Stop when the quotient is 0.
Read the remainders from bottom to top which represents the digits from left to right.

Subtraction in a computer is done with 2's complement arithmetic
1. First pad out both numbers with 0 up to the specified bit size
2. Take the Number being subtracted and toggle all the bits and add 1
3. Add the resulting number to the number it is being subtracted from

 1100 -->  00001100
 -111 --> -00000111
 
 SUBTRACTION
  01111010        
 -00000101
 --------
 11111010
 +      1
 --------
  11111011
- 01111010
 --------
 1(01110101)
 
 Multiplication start in the first place then multiply through.
 Then do the second place add a 0 then do 
  1011
x 1101
------
   1011
 101100
1011000
-------
10001111

DeMorgan's Law 
_ _   ___
x y = x+y
__   _ _
xy = x+y
"""