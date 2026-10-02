"""
grade_utils.py
Custom module for student grade calculations.
"""

def calculate_percentage(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def determine_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"