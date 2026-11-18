students = {}


def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    course = input("Enter Course: ")

    marks = []

    for i in range(5):
        mark = int(input(f"Enter marks for Subject {i + 1}: "))
        marks.append(mark)

    students[roll] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def display_student(roll):
    if roll in students:
        print(students[roll])
    else:
        print("Student not found!")


def display_all_students():
    if not students:
        print("No students available.")
    else:
        for roll, details in students.items():
            print("Roll Number:", roll)
            print("Name:", details["name"])
            print("Course:", details["course"])
            print("Marks:", details["marks"])
            print()


def search_student(roll):
    display_student(roll)


def update_student(roll):
    if roll in students:
        print("1. Update Name")
        print("2. Update Course")
        print("3. Update Marks")

        choice = input("Enter choice: ")

        if choice == "1":
            students[roll]["name"] = input("Enter new name: ")

        elif choice == "2":
            students[roll]["course"] = input("Enter new course: ")

        elif choice == "3":
            marks = []

            for i in range(5):
                mark = int(input(f"Enter marks for Subject {i + 1}: "))
                marks.append(mark)

            students[roll]["marks"] = marks

        else:
            print("Invalid choice!")
            return

        print("Student updated successfully!")
    else:
        print("Student not found!")


def delete_student(roll):
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")