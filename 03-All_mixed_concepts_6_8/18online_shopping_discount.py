amount = float(input("Enter purchase amount: "))
prime = input("Prime member? (yes/no): ")
coupon = input("Coupon available? (yes/no): ")

if amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

amount = amount - discount

if prime == "yes":
    amount = amount - amount * 0.05

if coupon == "yes":
    amount = amount - amount * 0.10

if amount >= 500:
    shipping = 0
else:
    shipping = 50

amount = amount + shipping

print("Final Amount =", amount)

if shipping == 0:
    print("Free Shipping")
else:
    print("Shipping Charge = ₹50")