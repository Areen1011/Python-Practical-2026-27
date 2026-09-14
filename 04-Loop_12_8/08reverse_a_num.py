num = int(input("Enter the number: "))
i = 0
while num > 0:
    digit = num % 10
    i = (i * 10) + digit
    num = num // 10
print(i)
print(num)