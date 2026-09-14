marks =[]

for i in range(5):
    mark = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)
    
print("All marks: ", marks)

index = int(input("Enter index to see marks: "))

print(marks[index])

newmark = int(input("Enter new marks for index 2: "))

marks[2]= newmark

print("Updates list: ", marks)