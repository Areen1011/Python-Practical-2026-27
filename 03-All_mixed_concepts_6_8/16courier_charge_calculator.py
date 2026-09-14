weight = float(input("Enter weight in kg: "))
distance = int(input("Enter distance in km: "))
express = input("Express delivery? (yes/no): ")

if weight <= 1:
    charge = 50
elif weight <= 5:
    charge = 80
elif weight <= 10:
    charge = 120
else:
    charge = 150

if distance > 500:
    charge = charge + (distance - 500) * 2

if express == "yes":
    charge = charge + charge * 0.40

print("Courier Charge =", charge)