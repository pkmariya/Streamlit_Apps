
bird_names = ["Dove", "Cuckoo", "Crow", "Sparrow", "Eagle"]

bird_guess = input("Guess a bird name")

x = [bird.lower() for bird in bird_names]

if bird_guess.lower() in x:
    print(bird_guess, " is in the Birds list")
else:
    print(bird_guess, " is not the in the list, try again!")