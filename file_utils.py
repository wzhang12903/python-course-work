"""
file_utils.py
This module handles file input and output for student records.
It allows saving and loading student data.
"""

def save_student(name, average, grade, filename="students.txt"):
    """Save student information to a file."""
    with open(filename, "a") as file:
        file.write(f"{name}, {average:.2f}, {grade}\n")


def read_students(filename="students.txt"):
    """Read and display student records."""
    try:
        with open(filename, "r") as file:
            print("\nSaved student records:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student records found.")
