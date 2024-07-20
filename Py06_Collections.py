
#Array
myList = ["List:", "Mango", "JackFruti", "Banana"]

#Tuple
myTuple = ("Tuple:", "Mango", "JackFruit", "Banana")

#Dictionary
myDict = {"Name": "Mariya", "Location": "Chennai"}

print()

print(myList)
print(myTuple)
print(myDict)

print()

print("Type of myList is:", type(myList))
print("Type of myTuple is:", type(myTuple))
print("Type of myDict is:", type(myDict))

print()

def display(collection):
    print("List of items are:")
    for item in collection:
        print(item)


display(myList)
print()

display(myTuple)
print()

display(myDict)
print()