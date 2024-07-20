

class parent:
    parentAttr = 100

    def __init__(self):
        print "Parent class constructor"

    def parentMethod(self):
        print "Parent Method"

    def setAttr(self):
        self.parentAttr = 200

    def getAttr(self):
        print "Parent Attribute is: ", self.parentAttr

class child(parent):
    childAttr = 50

    def __init__(self):
        print "Child class constructor"

    def childMethod(self):
        print "Child Method"


c1 = child()
#c1.parentMethod()
#c1.setAttr()
#c1.getAttr()

if issubclass(child, parent):
    print "is a subclass"

if isinstance(c1, parent):
    print "is an object of parent"
else:
    print "is an object of child"


"""
class parent:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        parent.empCount += 1


    def display(self):
        print "Name:", self.name, "Salary:", self.salary

    def dispCount(self):
        print "Total employees count is: ", self.empCount

    def __del__(self):
        print self.__class__.__name__, "class destroyed"

class child(parent):
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def display(self):
        print "Name: ", self.name, "Salary: ", self.salary, "Age :", self.age

emp1 = parent("Mariya", 123456)
emp2 = child("Preeths", 231456, 39)

emp1.display()
emp2.display()

emp2.dispCount()

"""