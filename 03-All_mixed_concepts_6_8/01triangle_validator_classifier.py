a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# if a + b > c and a + c > b and b + c > a:

#     print("Valid Triangle")

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Right")
elif a*a + b*b > c*c and a*a + c*c > b*b and b*b + c*c > a*a:
    print("Acute")
else:
    print("Obtuse")
