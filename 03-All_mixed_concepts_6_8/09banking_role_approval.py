salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))
loan = int(input("Enter existing loan: "))
years = int(input("Enter employment years: "))

if salary >= 40000 and credit >= 700 and years >= 2 and loan <= 500000:
    print("Approved")

elif salary >= 30000 and credit >= 650 and years >= 1 and loan <= 500000:
    print("Conditionally Approved")

else:
    print("Rejected")

    if salary < 30000:
        print("Reason: Salary is too low")
    if credit < 650:
        print("Reason: Credit score is too low")
    if years < 1:
        print("Reason: Employment experience is too low")
    if loan > 500000:
        print("Reason: Existing loan is too high")