
def accum(s):
    var = ""
    n = len(s)  #length of the string
    for i in range(n):  #Outer loop to consider each character in the string.
        for j in range(i+1):    #Loop to print each element in the string the number of times their position occurs.
            if j == 0:  #Always capitalise the first letter
                var += s[i].upper()
            else:   #Subsequent letters are in lower case.
                var += s[i].lower()
        if i < n-1: #To ensure the program doesn't print the '-' after the last string group. 
            var += '-'
    return var

print(accum("ZpglnRxqenU"))
    
