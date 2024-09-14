#Assignments: Python OOP Fundamentals
'''
1. City Infrastructure Management System

Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build 
a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods,
 and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and 
demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
- Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script
 showing the creation of Vehicle objects and updating their owners.

'''
class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
    #Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
        def update_owner(self, owner):
              name = input("Please enter the first and last name of the owner. Example -- John Smith? ")
              owner = name
              self.owner = owner
              print("The name of the vehicle's owner has been updated.")
              
vehicle1 = Vehicle(111, "Toyota", "John Smith")
vehicle2 = Vehicle(4854902, "Honda", "Luke Michael")

vehicle1.update_owner("Daniel Kassaye")
print()
print(vehicle1.registration_number)
print(vehicle1.type)
print(vehicle1.owner)
