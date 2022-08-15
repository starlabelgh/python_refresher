t = 5, 11
x, y = t

print(x, y)


student_attendance = {"Rolf": 96, "Moses": 34, "Akua": 56, "Esther": 27}

#print(list(student_attendance.item()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
    
    
people = [("Bob", 42, "Mechanic"), ("Moses", 28, "IT"), ("Esther", 26, "Security")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
    

for person in people:
    print(f"Name: {person[0]}, Age: {age[1]}, Profession: {profession[2]}")
    
    
person = ("Bob", 42, "Mechanic")
name, _, profession = person

#print(person)
print(name, profession)


*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)