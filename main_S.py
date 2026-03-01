"""
main.py
Main program for the Student Record Manager.
It imports custom modules and uses built-in libraries.
"""

# Import style 1
import grade_utils

# Import style 2
from file_utils import save_student, read_students

# Built-in library
import datetime

print("Student Record Manager")
print("Date:", datetime.date.today())

while True:
    name = input("\nEnter student name (or 'quit' to exit): ")
    if name.lower() == "quit":
        break

    grades = []

    # collect grades
    for i in range(3):
        score = float(input(f"Enter score {i+1}: "))
        grades.append(score)

    # use module functions
    avg = grade_utils.calculate_average(grades)
    grade = grade_utils.letter_grade(avg)

    print(f"{name}'s average: {avg:.2f}, Grade: {grade}")

    # save data
    save_student(name, avg, grade)

# read saved records
read_students()

print("Program finished.")