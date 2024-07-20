
num_animals = 0
all_animals = []

print("* * * Enter \"exit\" to exit out of the loop")

while True:
    animal_name = input("enter an animal name")
    if animal_name != "exit":
        all_animals.append(animal_name.capitalize())
        num_animals += 1
    else:
        break

print(all_animals)
