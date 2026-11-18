import arithemetic
from arithemetic import add, subtract
from student import student_details, student_result

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", arithemetic.multiply(10, 5))
print("Division:", arithemetic.divide(10, 5))

print("\nStudent Details")
student_details("Areen", 101)

print("\nStudent Result")
student_result([80, 90, 85])
