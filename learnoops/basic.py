# class Car:
#     pass
# my_car = Car()  

# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# # Creating an object

# s1 = Student("Alice", 101)
# print(s1.name)   # Output: Alice
# print(s1.roll)   # Output: 101



# Adding Methods (Functions inside a class)==================


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

s1 = Student("Bob", 102)
s1.show_details()  # Output: Name: Bob, Roll No: 102




# Inheritance (Reusability)=======================

class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking.")

class Student(Person):  # Student inherits from Person
    def study(self):
        print(f"{self.name} is studying.")

s1 = Student("Eva")
s1.speak()   # Eva is speaking.
s1.study()   # Eva is studying.
