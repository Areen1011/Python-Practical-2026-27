age = int(input("enter age: "))
salary = int(input("Enter monthly salary: "))

if 21 <= age <= 60 and salary >= 30000:
    print("You are eligible for loan")
else:
    print("You are not eligible to loan")
