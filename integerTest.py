def prompt(query):
	print(query)
	var = input()
	return(var)
	
test1 = "Input the number which you want to test:"
test2 = 'Do you want to continue? (Y/N):'

def integerTest():
	num = prompt(test1)
	var = ((num + ' is an integer.') if ((num % 1) == 0) else (num + ' is not an integer.'))
	print(var)

var = True

while (var):
	integerTest()
	check = prompt(test2)
	var = True if (check == 'Y' or check == 'y') else False


