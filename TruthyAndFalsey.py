#"Truthy" and "Falsey" values.
#"0", "0.0" and "''" are considered "False".
#All other values are considered true.

name = ''
while(not name):
    print('Enter your name:')
    name = input()

print('How many guests will you have?')
numOfGuests = int(input())
if(numOfGuests):
    print(name + ' ensure that you have enough room for all your guests.')

print('Done.')
