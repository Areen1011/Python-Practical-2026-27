try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division:", a / b)

    lst = [10, 20, 30]
    i = int(input("Enter list index: "))
    print("List Element:", lst[i])

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

except IndexError:
    print("Invalid list index")

else:
    print("No exception occurred")

finally:
    print("Program execution completed")

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("You are eligible")

except ValueError as e:
    print("Error:", e)
