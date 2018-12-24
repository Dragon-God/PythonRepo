i = 1
a = 1
b = 1

print('Input the number of terms of the fibonacci sequence you want to see:')
max = int(input())

while(i < max):
    print('Term ' + str(i) + ' of the Fibonacci sequence is: ' + str(a) + '.\n')
    print('Term ' + str(i + 1) + ' of the Fibonacci sequence is: ' + str(b) + '.\n')
    a += b
    b += a
    i += 2

print('\nDone.\n')    
