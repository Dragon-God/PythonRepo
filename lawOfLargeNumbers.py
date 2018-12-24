#This is a program to test the law of large numbers.

import random

print('Input the large number:')
large = int(input())
print('Input the minimum value for the range:')
mini = int(input())
print('Input the maximum value for the range:')
maxi = int(input())

n = 0

#Create an associative array mapping each of the numbers in the range to their probabilities.
#When a number is printed, look it up in the array, and update the element it maps to accordingly.

for i in range(large):
    
