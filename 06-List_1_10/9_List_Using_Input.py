num=int(input("How many numbers do you want to enter? "))

lst=list()

for i in range(num):
    a=int(input("Enter numbers: "))
    lst.append(a)

print(lst)
print(len(lst))
print(lst[0])
print(lst[-1])