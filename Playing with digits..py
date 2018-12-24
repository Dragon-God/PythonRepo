#a^n = n*a^(n-1) = (n-1)a^(n-1) + a(n-1)
# The idea is to generate some array containing the digits to their respective powers.
#Subsequently summing the new array, and then taking its modulus base n.

def sumc(value):  #Function to sum the elements of an array.
    n = len(value)
    sumc = 0
    for i in range(n):
        sumc += value[i]
    return sumc

def sumx(values, p): #sums the desired array.
    n = len(values)
    for i in range(n):  #changes each member of the array so that the elements of the array are in ascending order of powers.
        values[i] **= (p+i)
    return sumc(values)

def splice(num):     #Function to split a number up into an array of digits.
    num = str(num)
    n = len(num)
    var = [None]*n
    for i in range(n):
        var[i] = int(num[i])
    return var
    

def dig_pow(n, p):
    no = splice(n)
    result = sumx(no, p)
    if (result % n) != 0:    #If the result is not a multiple of n.
        return -1
    else:
        return int(result/n)

print(dig_pow(695,2))
