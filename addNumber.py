
def get_nums():
	num1 = input("Enter first value:\n")
	num2 = input("Enter second value:\n")
	return num1, num2

def add_nums():
	val1, val2 = get_nums()
	sum = int(val1) + int(val2)
	return sum

print("Sum of given numbers is: ", add_nums())