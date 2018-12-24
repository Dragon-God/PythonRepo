# This program says hello and asks for my name.
print('Hello world! \n')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName + '\n')
print('The length of your name is: ' + str(len(myName)) +'\n')

print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year. \n')
