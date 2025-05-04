class Student:
    def __init__(self, name, grade, percentage, team):
        self.name = name
        self.grade = grade
        self.percentage = percentage
        self.team = team
    
    def student_detail(self):
        print(f"{self.name} is in class {self.grade} with {self.percentage}% and is in the team {self.team}")

team1 = "A"
team2 = "B"

s1 = Student("Ali", 8, 86.9 , team1)
s1.student_detail()

s2 = Student("hamza", 8, 70.9 , team2)
s2.student_detail()