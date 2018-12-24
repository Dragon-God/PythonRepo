def spam(div):
    try:    #Code that may potentially cause an error. WIll execute as normal if no error occurs.
        return 42/div
    except ZeroDivisionError:   #Code that may potentially cause an error. Will get called if an error occurs.
        print("Error: Invalid argument, division by zero is not possible.")

print(spam(2))
#print(spam(0))
print(spam(21))

#Errors that occur in function calls would also be caught. For example:
#try:
#   spam(0)
#except:
#   print("Error: Invalid argument, division by zero is not possible.")
#Would output "Error: Invalid argument, division by zero is not possible."
