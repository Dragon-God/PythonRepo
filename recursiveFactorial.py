import sys
sys.setrecursionlimit(1000)

def fact(n): #takes the factorial of a number.        
    return 1 if (n == 0) else n*fact(n-1)

print('Input the number you want to find the factiorial of')
number = int(input())

print(str(number) + '! is: \t' + str(fact(number)))
