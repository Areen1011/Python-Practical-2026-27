import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
op = sys.argv[3]

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero is not possible")
else:
    print("Invalid operator")
