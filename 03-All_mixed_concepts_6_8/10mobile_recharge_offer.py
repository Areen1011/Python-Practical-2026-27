amount = int(input("Enter recharge amount: "))
student = input("Are you a student? (yes/no): ")
festival = input("Is festival offer available? (yes/no): ")

if amount < 199:
    print("Not eligible for any offer")
elif amount <= 299:
    print("1 GB/day")
elif amount <= 499:
    print("2 GB/day")
elif amount <= 999:
    print("3 GB/day")
else:
    print("Unlimited benefits")
if student == "yes":
    print("Student discount available")
if festival == "yes":
    print("Festival cashback available")