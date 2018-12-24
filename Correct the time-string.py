def stm(var):   #A function to make politically correct strings.
    if var < 10:
        return '0' + str(var)
    else:
        return str(var)

def time_correct(t):
    if (t is None) or (len(t) == 0):
        return t
    n1 = len(t)
    
    if n1 != 8: #Checks if the string is valid (length-wise)
        return None
    
    try:    #Checks if the string is valid (the right digits are numbers).
        n3 = int(t[0]+t[1]+t[3]+t[4]+t[6]+t[7])
    except ValueError:
        return None
    
    v1 = int(t[0] + t[1])
    v2 = int(t[3] + t[4])
    v3 = int(t[6] + t[7])
    n2 = t[2] + t[5]
    s = (v1 * 3600) + (v2 * 60) + v3 #Convert the time to seconds.
    if (n2 != "::"): #Checks if the string is valid by checking that the ":" are in the right places, and the time doesn't give more than 86400 seconds in a day.
        return None
    else:
        s %= 86400 #Normalises the time to the correct format.
        j1 = s // 3600 #Checks the number of hours in the string.
        s %= 3600
        j2 = s // 60 #Checks the number of minutes.
        s %=  60
        j3 = s #Checks the number of seconds.
        s = stm(j1) + ":" + stm(j2) + ":" + stm(j3)
        return s

print('Input the time string that needs to be converted to the proper format: \t')
t = input()    
print('The correct time is: \t \"' + time_correct(t) + '\"')
