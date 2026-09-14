year1 = int(input("Enter first year: "))
year2 = int(input("Enter second year: "))

if (year1 % 4 == 0 and year1 % 100 != 0) and (year2 % 4 == 0 and year2 % 100 != 0):
    print("Both are leap years")
elif year1 % 4 == 0 and year1 % 100 != 0:
    print("First year is leap year")
elif year2 % 4 == 0 and year2 % 100 != 0:
    print("Second year is leap year")
else:
    print("Both are not leap years")
