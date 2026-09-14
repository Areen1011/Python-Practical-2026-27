password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0
count = 0

for ch in password:
    count = count + 1

    if ch >= 'A' and ch <= 'Z':
        upper = 1
    elif ch >= 'a' and ch <= 'z':
        lower = 1
    elif ch >= '0' and ch <= '9':
        digit = 1
    else:
        special = 1

if count < 8:
    print("Weak")
elif upper == 1 and lower == 1 and digit == 1 and special == 1:
    print("Strong")
else:
    print("Medium")