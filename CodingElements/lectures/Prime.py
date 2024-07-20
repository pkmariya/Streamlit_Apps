
# Find the Prime number. A number is Prime if it's divisble by anything other than 1 and the number itself.

num = int(input("Enter a number"))

# def findPrime(num):
#     isPrime = True
#
#     for i in range(2, int(num**0.5)+1):
#         if (num%i == 0):
#             isPrime = False
#             break;
#
#     if (isPrime):
#         print("{} is a Prime number".format(num))
#     else:
#         print("{} is not a Prime number".format(num))
#
# findPrime(num)


for i in range(2, num):
    j = i
    for j in range(1, i):
        if (i%j != 0):
            print(i)
