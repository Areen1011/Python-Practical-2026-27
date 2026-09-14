num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

if 10 <= num <= 99 or -99 <= num <= -10:
    print("Two-digit number")
elif 100 <= num <= 999 or -999 <= num <= -100:
    print("Three-digit number")
elif 1000 <= num <= 9999 or -9999 <= num <= -1000:
    print("Four-digit number")
else:
    print("Not a 2, 3 or 4 digit number")

if 0 <= num <= 9:
    print("Palindrome")
elif 10 <= num <= 99:
    if num // 10 == num % 10:
        print("Palindrome")
    else:
        print("Not Palindrome")
elif 100 <= num <= 999:
    if num // 100 == num % 10:
        print("Palindrome")
    else:
        print("Not Palindrome")
elif 1000 <= num <= 9999:
    if num // 1000 == num % 10 and (num // 100) % 10 == (num // 10) % 10:
        print("Palindrome")
    else:
        print("Not Palindrome")
else:
    print("Palindrome check not available")