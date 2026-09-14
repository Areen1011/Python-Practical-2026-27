a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation")

else:
    d = b * b - 4 * a * c

    if d > 0:
        print("Real and distinct roots")
    elif d == 0:
        print("Real and equal roots")
    else:
        print("Imaginary roots")