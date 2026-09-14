num = int(input("Enter the number of elements: "))

list=[]

for i in range(num):
    i = int(input(f"Enter {i + 1} elements: "))
    list.append(i)
    
print(list)
print("Length of list is: ", len(list))
print("First element: ", list[0])
print("Last element: ", list[num-1])