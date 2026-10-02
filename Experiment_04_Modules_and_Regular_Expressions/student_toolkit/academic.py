# Academic Module
# Functions for calculating student performance

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)