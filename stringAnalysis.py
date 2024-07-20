
def str_analysis(test_str):
    if test_str.isalpha():
        print("\"", test_str, "\"", " is all alphabetical")
    elif test_str.isdigit():
        if int(test_str) > 99:
            print(test_str, " is a pretty big number")
        elif int(test_str) < 99:
            print(test_str, " is a smaller number than expected")
    else:
        print(test_str, " is neither alpha nor all digit")


str = input("enter word or integer")

while str =="":
    str = input("enter word or integer")

str_analysis(str)