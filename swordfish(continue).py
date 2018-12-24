while True:
    print('Who are you?')
    name = input()
    if(name.lower() != 'tobi'):
        continue
    print('Hello ' + name + ' what is the password? (It is a fish):')
    password = input()
    if(password == 'Sw0rdfi$h'):
        break

print('Access Granted.')
