def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def cardinal(num):
    num = str(num)
    n = len(num)
    if num[n-1] == '1':
        return 'st'
    elif num[n-1] == '2':
        return 'nd'
    elif num[n-1] == '3':
        return 'rd'
    else:
        return 'th'

    
print('Input the number of the fibonacci sequence you want to find: \t')
num = input()
num = int(num)
val = fib(num)
print('The ' + str(num) + cardinal(num) + ' number of the Fibonacci sequence is: ' + str(val))
