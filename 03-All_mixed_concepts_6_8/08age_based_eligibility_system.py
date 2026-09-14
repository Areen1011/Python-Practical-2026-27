age = int(input("Enter your age: "))
gender = input("Enter gender (male/female): ")

if age < 0:
    print("Invalid age")

else:
    if age >= 5 and age < 18:
        print("Eligible for School")
    if age >= 18:
        print("Eligible for Driving Licence")
    if age >= 18:
        print("Eligible for Voting")
    if gender == "male" and age >= 21:
        print("Eligible for Marriage")
    elif gender == "female" and age >= 18:
        print("Eligible for Marriage")
    else:
        print("Not eligible for Marriage")
    if age >= 60:
        print("Eligible for Senior Citizen Benefits")