#This is a function to simulate the collatz sequence.

def collatz(number):
	return (number//2) if (number % 2 == 0) else ((3*number)+1)

while True:
	try:
		print("Input the number: ", end="")
		num = int(input())
		i = num
		break
	except ValueError:
		print("Error: Invalid input.\n Please input a whole number.")
		continue

while True:
	pass
	i = collatz(i)
	print(i)
	if(i == 1):
		break