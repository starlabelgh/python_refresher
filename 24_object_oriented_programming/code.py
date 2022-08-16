import struct


student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence)/ len(sequence)

print(average(student["grades"]))



#opp

class Student:
    def __init__(self) -> None:
        self.name = "Moses"
        self.grades = (90, 99, 93, 78, 90)
        
    def average(self):
        return sum(self.grades)/len(self.grades)
        
        
student = Student()
print(Student.average(student))