attendance = int(input("Enter attendance in %: "))
marks = int(input("Enter marks of the student: "))
income = int(input("Enter family income in Rs: "))
category = input("Enter category (General/Sports): ")

if attendance >= 90 and marks >= 85 and income <= 500000 and category.lower() == "general":
    print("The student is eligible for scholarship, as he has good attendance, marks and family income.")
    if category.lower() == "sports":
        marks += 5
        print("The student got grace marks for sports category. New marks: ", marks)
        print("The student is eligible for scholarship., as he has good attendance, marks and family income.")
elif attendance <= 75:
    print("The student is not eligible for scholarship, as he has poor attendance.")