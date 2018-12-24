#importing modules in Python
#Syntax:
#"import moduleName, ..."
#OR
#"from moduleName import *"
#Using the above allows you to use functions inside a module without prefixing them with "moduleName.".

import random

while True:
    print('Input the minimum value for the range:')
    mini = int(input())
    print('Input the maximum value for the range:')
    maxi = int(input())
    var = random.randint(mini, maxi)
    print('The random number is: ' + str(var) + '.')

    print('Do you want to continue (Y/N)?')
    test = input()
    if(not(test.lower() == 'y' or test.lower() == 'yes')):
        break

    
    
