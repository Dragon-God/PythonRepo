#This is a guess the number program.

import random
import math

while True:     #Outer loop that controls the game.
    while True:     #Loop for correct input.
        pass
        print("Input the maximum number: ", end="")
        try:    #Clause to accept user input.
            maxi = int(input())
            maxi += 1
            break
        except ValueError:
            print("Error: Invalid input.\n Please input a whole number.")
            continue

    while True:     #Loop for game play.
        num = random.randrange(maxi)
        print("I am thinking of a number between " + str(0) + " and " + str(maxi-1) + " (both inclusive).")
        count = 0
        while(count < (2 * math.ceil(math.log(num, 2)))):
            try:
                print("Take a guess: ", end="")
                guess = int(input())
                count += 1
            except ValueError:
                print("Error: Invalid input.\n Please input a whole number.")
                continue

            if(guess < num):
                print("Your guess is to low.")
            elif(guess > num):
                print("Your guess is to high.")
            else:
                break

        if(guess == num):
            print("Good job! You guessed my number in " + str(count) + " guesses!")
        else:
            print("Nope. The number I was thinking of was " + str(num) + ".")

        print("Do you want to play again? (Y/N)")
        check1 = input().lower()

        if(check1 == "y" or check1 == "yes"):
            print("Do you want to use the same range? (Y/N)")
            check2 = input().lower()
            if(check2 == "y" or check2 == "yes"):
                print("\n\n")
                continue
            else:
                break
        else:
            break
        
    if(check1 == "y" or check1 == "yes"):
        print("\n\n")
        continue
    else:
        break

