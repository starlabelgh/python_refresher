friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Bob"] = 20

print(friend_ages)



friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Moses", "age": 28},
    {"name": "Akua", "age": 21}
]

print(friends)
print(friends[1]["name"])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
                                                                    
# for student, attendance in student_attendance.items():
#     print(f"{"Bob:"}: {student_attendance["Bob"]}")

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")
    

attendance_values = student_attendance.values()
print(sum(attendance_values)/len(attendance_values))