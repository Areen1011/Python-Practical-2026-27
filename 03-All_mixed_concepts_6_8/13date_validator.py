day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid Date")

elif day < 1:
    print("Invalid Date")

elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if day <= 29:
            print("Valid Date")
        else:
            print("Invalid Date")
    else:
        if day <= 28:
            print("Valid Date")
        else:
            print("Invalid Date")

elif month == 4 or month == 6 or month == 9 or month == 11:
    if day <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")

else:
    if day <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")