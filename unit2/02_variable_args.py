def student_result(name, *marks, **info):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    return total, average, highest

name = input("Enter student name: ")
roll = input("Enter roll number: ")
clas = input("Enter class: ")

marks = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

total, average, highest = student_result(
    name, *marks, roll=roll, class_name=clas
)

print("\n--- Student Result ---")
print("Name:", name)
print("Roll Number:", roll)
print("Class:", clas)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
