'''
This is a note for Module 4 of Python Intermediate. 
This is a Multi-line String comment. 

Lesson 2 : OOP Fundamentals

https://www.w3schools.com/python/python_classes.asp

'''

# Python is an object oriented programming language.

# OOP(Object-Oriented Programming): brings structure and clarity to code --> 
    # Modularity --> OOP divides a program into modules or objects.
    # Reuse --> OOP allows code reuse
    # Maintenance --> OOP's encapsulation allows you to update a targeted section of code instead of all of it.
    # Scalability --> OOP allows you to scale your application by adding new objects. Allows expansion of software

    
# A Class is like an object constructor, or a "blueprint" for creating objects. It describes the structure and behaviour of an object. 

# The Constructor is a special method named __init__.
# The Destructor to destroy object state named __del__. 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(p1)

# An object is a specific instance of a class. 

# Procedural Programming --> specific steps while OOP like road connects buildings, the connections between different objects. 


# Example Defining Classes in Python Video 
print()
class OfficeBuilding:
  def __init__(self, floors, offices):
    self.floors = floors
    self.offices = offices

  def open_doors(self):
    print("Doors are open for business!")

building1 = OfficeBuilding(10, 200)
building2 = OfficeBuilding(20, 400)

building1.open_doors() 