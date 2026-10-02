# Attendance Module
# Functions for calculating student attendance

def attendance_percentage(attended, total_classes):
    if total_classes <= 0:
        return 0

    return (attended / total_classes) * 100


def check_eligibility(percentage):
    if percentage >= 75:
        return "Eligible"
    return "Not Eligible"