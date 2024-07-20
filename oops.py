

class Vehicle:
    def __init__(self):
        return None
    
    def __str__(self):
        return "Main Class"
    
    def display(self):
        return "display function from Main Class"
    
class Car:
    def __init__(self):
        super().__init__()
        return None
    
    def display(self):
        return "display function from Car Class"
    

vehicle_obj = Vehicle()
print(vehicle_obj.display())

car_obj = Car()
print(car_obj.display())




