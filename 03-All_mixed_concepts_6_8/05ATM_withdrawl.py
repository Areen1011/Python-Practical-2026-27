balance = int(input("Enter account balance: "))
amount = int(input("Enter withdrawal amount: "))
pin = int(input("Enter PIN: "))

correct_pin = 1234

if pin != correct_pin:
    print("Incorrect PIN")

elif amount > 20000:
    print("Maximum withdrawal is ₹20,000")

elif amount % 100 != 0:
    print("Amount must be a multiple of 100")

elif balance - amount < 1000:
    print("Insufficient balance")

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)