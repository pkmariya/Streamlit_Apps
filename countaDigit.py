
digit = 1
limit = 0
digit = int(input("Enter a digit that you want to count\n"))
limit = int(input("Enter the limit\n"))

count1, count2, count3, count4 = 0, 0, 0, 0

for i in range(1, limit):
    if int(i) == digit:
        count1 += 1
    elif int(i/10) == digit:
        count2 += 1
        if int(i%10) == digit:
            count3 += 1
    elif int(i%10) == digit:
            count4 += 1

print("\n", digit, "appears ", count1+count2+count3+count4, " times!")