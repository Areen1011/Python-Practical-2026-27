print("Calculator")
print("Addition: 1, Subtraction: 2, Division: 3, Multiplication: 4")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = int(input("Enter choice: "))

if choice == 1:
    print("Addition is: ", num1 + num2)
elif choice == 2:
    print("Subtraction is: ", num1 - num2)
elif choice == 3:
    print("Division is: ", num1 / num2)
elif choice == 4:
    print("Multiplication is: ", num1 * num2)
else:
    print("You entered wrong choice")
