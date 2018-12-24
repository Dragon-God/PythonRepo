#Take the array of strings.
#FInd the length of the array.
#The number of consecutive strings = n - k + 1.

def longest_consec(strarr, k):
    n = len(strarr)
    var = []    #create a list to contain the different strings.
    if n == 0 or k > n or k <= 0: #Some failure conditions.
        return ""

    else:
        c = n - k + 1    #A control variable. Contains the number of possible strings formed by concatenating k consecutive strings.
        for i in range(c):  #Loop to set default element of the list to empty strings: seeding it basically.
            var.append("")     
        for i in range(c):  #Outer loop, controls the individual elements of the list.
            for j in range(i,(i+k)):  #Inner loop, that is used to make each element of the list a cocatenation of some set of consecutive strings.
                var[i] += strarr[j]

    max = var[0]    #Variable to keep count of the longest string found so far.
    for i in range(1,c):    #Checks if string is longer than current maximum. If yes, resets current maximum.
        if len(var[i]) > len(max):
            max = var[i]

    return max

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
