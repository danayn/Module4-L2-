'''
This is a note for Module 4 of Python Intermediate. 
This is a Multi-line String comment. 

Lesson 2 : OOP Fundamentals

https://www.w3schools.com/python/python_classes.asp

'''

# Python is an object oriented programming language.

# A Class is like an object constructor, or a "blueprint" for creating objects.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(p1)