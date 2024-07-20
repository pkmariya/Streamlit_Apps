# List as Arrays and associated Methods


cars = ["Ford Ecosport", "Honda Civic", "Maruti Swift", "Toyota Innova", "Tata Sumo"]

print()

cars.append("Hyundai Verna")
cars.insert(1, "BMW")
cars.sort()
print("Length of cars array is:", len(cars))
print("List of cars in the array are:", cars)
print("Index of Innova is:", cars.index("Toyota Innova"))

print()
print("List of Cars in cars Array are:")
for car in cars:
    print(car)

#cars.pop(1)



print()



