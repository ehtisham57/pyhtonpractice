# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Abstraction ---hiding un necessory thing from user through method or object


class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade =  grade
        self.percentage = percentage
    
    def show_data(self): # Abstraction
        print(f"Student name is {self.name}, Student Class is {self.grade} & Student percentage is {self.percentage}")


s1 = Student("ali" , 7 , 90)
s1.show_data()


