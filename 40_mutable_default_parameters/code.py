from typing import List, Optional
#from unicodedata import name

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None) -> None:
        self.name = name
        self.grades = grades or []
        
    def take_exam(self, result: int):
        self.grades.append(result)
        
        
moses = Student("Moses")
akua = Student("Akua")
moses.take_exam(90)
print(moses.grades)
print(akua.grades)