student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}


def average_grade(data):
    grades = data['grades']
    return sum(grades)/len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        #implement here
        total += sum(student['grades'])
        count += len(student['grade'])
        
        ans = total / count
        
    return ans