num = 12321
temp = num
i = 0
while num > 0:
    digit = num % 10
    i = (i * 10) + digit
    num = num // 10
print(i)
if i == temp:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")