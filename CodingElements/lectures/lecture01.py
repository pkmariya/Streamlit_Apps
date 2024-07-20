
#
# for i in range(0, 10, 2):
#     print(i, end=' ')


# for i in range(1, 6):
#     print('* ' * i)

# temp = ord('A')
# for i in range(5):
#     for j in range(i+1):
#         print("%c"%(chr(temp)), end=' ')
#     print()
#     temp += 1

N = int(input("Enter the range"))

# *** Left aligned pyramid ***

# for r in range(1, N+1):
#     str = ""
#     for c in range(r):
#         str += "* "
#     print(str)

# *** Inverted left aligned pyramid ***

# for r in range(N, 0, -1):
#     str = ""
#     for c in range(r):
#         str += "* "
#     print(str)

# *** Center aligned pyramid ***

# spaces = N-1
# stars = 1
#
# for r in range(N, 0, -1):
#     print(" " * spaces + "* " * stars)
#     spaces -= 1
#     stars += 1

# spaces = N - 1
# stars = 1
#
# for r in range(1, N+1):
#     str = ""
#     for c in range(spaces):
#         str += ' '
#     for c in range(stars):
#         str += "* "
#     print(str)
#     spaces -= 1
#     stars += 1


for i in range(N):
    for j in range(N-i):
        if (j == 0 or i == 0 or j == N-i-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()