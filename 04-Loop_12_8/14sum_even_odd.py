num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)

if sum % 2 == 0:
    print("Sum is Even")
else:
    print("Sum is Odd")