num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive even number")
elif num > 0 and num % 2 == 1:
    print("The number is positive odd number")
elif num < 0 and num % 2 == 0:
    print("The number is negative even number")
elif num < 0 and num % 2 == 1:
    print("The number is negative odd number")
else:
    print("The number is '0'")
