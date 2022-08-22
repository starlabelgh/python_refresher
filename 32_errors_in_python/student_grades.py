def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return (dividend / divisor)
    


students = [
    {"name": "Moses", "grades": [75, 90]},
    {"name": "Akua", "grades": [50]},
    {"name": "Esther", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} average {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student average calculated --")
finally:
    print("-- End of student average calculation")