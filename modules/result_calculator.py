def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return calculate_total(marks) / 5


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def check_pass_fail(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"

    return "Pass"


def find_topper(students):
    if not students:
        return None

    topper = max(
        students.items(),
        key=lambda student: calculate_percentage(student[1]["marks"])
    )

    return topper


def calculate_class_average(students):
    if not students:
        return 0

    total = 0

    for student in students.values():
        total += calculate_percentage(student["marks"])

    return total / len(students)