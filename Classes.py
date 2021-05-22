# Essence of OOP is creation of classes
# Classes are object constructors (blueprints for objects) 
# Objects have properties and methods

class Person:
    # Create a class
    def __init__(self, fname, lname):
        # Add some properties to the class
        self.firstname = fname
        self.lastname = lname

    # Create a method
    def printname(self):
      print(self.firstname, self.lastname)

class Student(Person):
    # Create a child class inheriting properties and methods from parent class
    def __init__(self, fname, lname, year):
        # Using super(), the child class inherits all properties from the parent class
        super().__init__(fname, lname)
        # Additional property is added to child class
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

print(x.graduationyear) # Properties of objects can be printed
x.printname() # Methods are executed using brackets