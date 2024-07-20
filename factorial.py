
# Recursive Function to calculate the Factorial of a given number

def fact1(n):
    if n==1:
        return 1
    else:
        return n * fact1(n-1)

x = int(input("Please enter an Integer"))
print(f"Factorial of {x} is: ", fact1(x))
