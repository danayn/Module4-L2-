#Assignments: Python OOP Fundamentals
'''
Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date

NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the 
run button at the top, all code executes as intended. For example, if there are if statements, print statements, or 
for loops, they should function correctly and display output in the console as expected. If you have a function, 
make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the 
methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

'''
class Event:
        def __init__(self, name, date, count):
            self.name = name
            self.date = date
            self.count = count

        def add_participant(self):
            self.count = self.count + 1
            print("A participant has been added.")


        def get_participant_count(self):
            print("The total number of participants is: ")
            print(self.count)
        
Event1 = Event("Party", "10/13/2024", 2)
Event1.add_participant()
Event1.add_participant()
Event1.get_participant_count()