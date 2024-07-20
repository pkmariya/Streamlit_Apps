
tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
    if tickets%3==0:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")