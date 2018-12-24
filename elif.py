##Greeting Program

import datetime #Module dealing with datetime.

day = datetime.datetime.today().weekday() #Returns day of the week, where Monday is '0' and Sunday is '6'.

if(day == 0):
    greeting = ('Have a nice Monday!\n')
elif(day == 1):
    greeting = ('Have a nice Tuesday!\n')
elif(day == 2):
    greeting = ('Have a nice Wednesday!\n')
elif(day == 3):
    greeting = ('Have a nice Thursday!\n')
elif(day == 4):
    greeting = ('Have a nice Friday!\n')
elif(day == 5):
    greeting = ('Have a nice Saturday!\n')
elif(day == 6):
    greeting = ('Have a nice Sunday!\n')
else:
    greeting = ('Have a nice day!\n')

print(greeting)
