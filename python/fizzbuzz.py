# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:53:49 2021

This program prints each number from 1 to 100, each on its own line, 
but with the following modifications:
    1. If the number is divisible by 3, "Fizz" is printed instead
    2. If the number is divisible by 5, "Buzz" is printed instead
    3. If the number is divisible by both 3 and 5, "FizzBuzz" is printed instead

@author: Colin Monaghan
"""

for value in range(1,101):
    if(value % 15 == 0):
        print('FizzBuzz')
    elif(value % 5 == 0):
        print('Buzz')
    elif(value % 3 == 0):
        print('Fizz')
    else:
        print(value)
