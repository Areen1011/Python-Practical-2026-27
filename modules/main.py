from student_details import *
from result_calculator import *


while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student")
    print("2. Display Student Details")
    print("3. Display All Students")
    print("4. Search Student")
    print("5. Update Student Record")
    print("6. Delete Student Record")
    print("7. Calculate Student Result")
    print("8. Display Topper")
    print("9. Calculate Class Average")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        roll = input("Enter Roll Number: ")
        display_student(roll)

    elif choice == "3":
        display_all_students()

    elif choice == "4":
        roll = input("Enter Roll Number: ")
        search_student(roll)

    elif choice == "5":
        roll = input("Enter Roll Number: ")
        update_student(roll)

    elif choice == "6":
        roll = input("Enter Roll Number: ")
        delete_student(roll)

    elif choice == "7":
        roll = input("Enter Roll Number: ")

        if roll in students:
            marks = students[roll]["marks"]

            total = calculate_total(marks)
            percentage = calculate_percentage(marks)
            grade = calculate_grade(percentage)
            result = check_pass_fail(marks)

            print("Total Marks:", total, "/ 500")
            print("Percentage:", percentage, "%")
            print("Grade:", grade)
            print("Result:", result)
        else:
            print("Student not found!")

    elif choice == "8":
        topper = find_topper(students)

        if topper:
            print("Topper Name:", topper[1]["name"])
            print("Roll Number:", topper[0])
            print(
                "Percentage:",
                calculate_percentage(topper[1]["marks"])
            )
        else:
            print("No students available!")

    elif choice == "9":
        average = calculate_class_average(students)
        print("Class Average:", average, "%")

    elif choice == "10":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")