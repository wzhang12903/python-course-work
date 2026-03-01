"""
grade_utils.py
This module handles grade calculations and student performance.
It provides functions to compute averages and letter grades.
"""

def calculate_average(grades):
    """Return the average of a list of grades."""
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def letter_grade(score):
    """Convert a numeric score into a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    