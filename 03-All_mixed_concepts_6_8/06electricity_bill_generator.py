units = int(input("Enter units consumed: "))
payment = input("Online payment? (yes/no): ")

fixed = 100

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7
elif units <= 500:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10
else:
    bill = 100 * 5 + 200 * 7 + 200 * 10 + (units - 500) * 12

bill = bill + fixed

if units > 500:
    bill = bill + bill * 0.10

if payment == "yes":
    bill = bill - bill * 0.05

print("Electricity Bill =", bill)