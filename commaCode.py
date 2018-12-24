#This is a function to implode a list.

def construct(someList):    #Function to consstruct string out of a list.
    string = ""
    for i in someList[:(len(someList)-1)]:  #Iterates through a slice of the list that excludes the last value in the list.
        string += str(i)  #append values to the string.
        string += ", "

    string += "and "
    string += str(someList[(len(someList)-1)])
    return(string)

