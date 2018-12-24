print('What is your name?')
name = input()
name = name.lower()
print('What is your password?')
psswd = input()
if name == 'tobi':
    print('Hello Tobi.')
else:
    print('Hello Stranger.')
if psswd == 'Gr3@tness':
    print('Access Granted.')
else:
    print('Access Denied.')
