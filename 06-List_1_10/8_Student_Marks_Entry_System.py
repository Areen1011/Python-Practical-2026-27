marks = list()

for i in range(5):
    b = input("Enter 5 marks: ")
    marks.append(b)

print("all marks", marks)

index=int(input("Enter index: "))

print("student's marks", marks[index])

newmarks=int(input("Enter marks: "))

marks.append(newmarks)

print("Updated list: ", marks)