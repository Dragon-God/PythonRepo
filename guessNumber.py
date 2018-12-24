import random, sys

sys.setrecursionlimit(10000)    #I expect any troll who's trying to fuck with the program to give up before they reach 10,000.
control = True    #global variable to control the behaviour of the 'guessNumber()' function.
errors = 0    #To store the number of errors a user triggers.

def guessNumber(maxx):
    global errors
    global control
    try:
        maxx = float(maxx)    #Incase a cheeky user decided to submit floating point numbers.
        if int(maxx) != maxx:     #If they submitted a floating point number instead of an integer.
            print("Input whole numbers only.")
            errors += 1
            guessNumber(input('Input the Maximum number: \t'))  #Call a new instance of 'guessNumber()'
        else:   #If they indeed submitted a whole number.
                maxx = int(maxx)
    except ValueError:  #They didn't submit a whole number.
            print("Input whole numbers only.")
            errors += 1
            guessNumber(input('Input the Maximum number: \t'))  #Call a new instance of 'guessNumber()'

    if not control:    #control variable. If the program has already properly evaluated, it should terminate.
        return None
    
    print('I am thinking of a whole number between 1 and ' + str(maxx) + ' (both inclusive).')        
    num = random.randint(1, maxx)
    count = 0
    check = True
    var = None

    while check:
        print("Guess the number.")
        try:
            var = float(input())    #Incase a cheeky user decided to submit floating point numbers.
            if int(var) != var:     #If they submitted a floating point number instead of an integer.
                print("Input whole numbers only.")
                errors += 1
                continue
            else:   #If they indeed submitted a whole number.
                var = int(var)
        except ValueError:  #They didn't submit a whole number.
            print("Input whole numbers only.")
            errors += 1
            continue
        count +=  1
        if var == num:  #If they guess the number right.
            check = False
        elif var > num:
            print('Too high! \nTry a little lower.')
        elif var < num:
            print('Too low! \nTry a little higher.')

    print('Congratulations!!!\nYou guessed the number after ' + str(count) + " tries and triggering " + str(errors) + " errors.")
    control = False     #After every completed execution, we set control to false so that if the program it terminates and doesn't cause errors.
    return None

guessNumber(input('Input the Maximum number (integers only): \t'))
