

str = "xu7g3io4"

digits = []
chars = []

for letter in str:
    # try:
    #     num = int(letter)
    #     digits.append(num)
    # except Exception as e:
    #     chars.append(letter)
    # print(letter)
    if letter.isdigit():
        digits.append(letter)
    else:
        chars.append(letter)
digits.sort()
chars.sort()
print(digits)
print(chars)