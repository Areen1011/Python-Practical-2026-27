m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("Fail")
else:
    print("Percentage =", percentage)

    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B+")
    elif percentage >= 60:
        print("Grade: B")
    else:
        print("Grade: C")

    if percentage >= 75:
        print("Distinction")
    else:
        print("No Distinction")