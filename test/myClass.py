

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total # of employees is: %d", Employee.empCount)

    def displayEmployee(self):
        print("Name : " + self.name + ", Salary : ", self.salary, "Age is: ", self.age)

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, " destroyed"

emp1 = Employee("Mariya", 156789)
emp2 = Employee("Preeths", 212345)

setattr(emp1, 'age', 48)
emp2.age = 39
emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCount()

print
print "Docu String  :", Employee.__doc__
print "Class Name : ", Employee.__name__
print "Module : ", Employee.__module__

print "final line"
