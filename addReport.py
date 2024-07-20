

def adding_report(report_type):
    total = 0
    items = ""
    while True:
        val = input("Enter an integer or \"Q\" to quit")
        if val.isdigit():
            total += int(val)
            if report_type == "A":
                items = str(items) + "\n" + str(val)
        elif val == "Q":
            if report_type == "A":
                print("Items")
                print(items)
                print("Total")
                print(total)
            elif report_type == "T":
                print("Total")
                print(total)
            break
        else:
            print("\n invalid input")

print("\n Calling add report with A")
adding_report("A")
print("\n Calling add report with T")
adding_report("T")


"""

total = 0
items = []

def adding_report(report_type):
    if report_type == "A":
        print("Items")
        print(items)
        print("Total")
        print(total)
    elif report_type == "T":
        print("Total")
        print(total)


choice = input("Enter your choice a) \"A\" b) \"T\" c) \"Q\" to quit")

while True:
    if choice =="A":
        val = input("Enter an integer or \"Q\" to quit")
        if val == "Q":
            adding_report("A")
            break
        elif val.isalpha():
            print(val, " is invalid input")
        else:
            items.append(int(val))
            total += int(val)
    elif choice =="T":
        val = input("Enter an integer or \"Q\" to quit")
        if val == "Q":
            adding_report("T")
            break
        elif val.isalpha():
            print(val, " is invalid input")
        else:
            total += int(val)
    elif choice == "Q":
        print("Quitting the game")
        break
        
"""