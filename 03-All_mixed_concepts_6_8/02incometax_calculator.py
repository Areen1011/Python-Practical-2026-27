income = int(input("Enter annual income: "))

if income <= 1200000:
    tax = 0
elif income <= 1600000:
    tax = (income - 1200000) * 0.15
elif income <= 2000000:
    tax = 60000 + (income - 1600000) * 0.20
elif income <= 2400000:
    tax = 140000 + (income - 2000000) * 0.25
else:
    tax = 240000 + (income - 2400000) * 0.30

if income > 10000000:
    tax = tax + tax * 0.15
elif income > 5000000:
    tax = tax + tax * 0.10

print("Tax payable =", tax)