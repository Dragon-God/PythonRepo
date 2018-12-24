#Collatz sequence.
check = True    #Control variable to control the recursion
def collatz(num):
    a = num // 2 if num%2 == 0 else (3*num)+1
    print(a)
    return a

def proof(var):
    global check
    try:
        var = float(var)
        if var != int(var):
            print("Please input only whole numbers.")
            proof(int(input("What is the number whose Collatz sequence you want to generate?  ")))
        else:
            var = int(var)            
    except ValueError:
        print("Please input only whole numbers.")
        proof(input("What is the number whose Collatz sequence you want to generate?  "))
    while check:    #While the sequence has not yet completed.
        var = collatz(var)
        if var == 1:
            check = False
    return None

proof(input("What is the number whose Collatz sequence you want to generate?  "))
