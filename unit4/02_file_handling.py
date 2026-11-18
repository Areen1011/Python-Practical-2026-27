f = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Marks: " + marks + "\n")

f.close()

f = open("student.txt", "r")
print("\nFile Contents:")
print(f.read())
f.close()

f = open("student.txt", "a")

name = input("Enter another student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

f.write("\nName: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Marks: " + marks + "\n")

f.close()

f = open("student.txt", "r")

print("\nAll Student Records:")
print(f.readlines())

f.close()

f = open("student.txt", "r")

print("\nReading Line by Line:")
for line in f:
    print(line, end="")

f.close()
