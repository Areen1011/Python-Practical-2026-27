x1 = int(input("Enter current x: "))
y1 = int(input("Enter current y: "))

x2 = int(input("Enter destination x: "))
y2 = int(input("Enter destination y: "))

if x1 == x2 and y1 == y2:
    print("Invalid move")

elif x2 >= x1 - 1 and x2 <= x1 + 1 and y2 >= y1 - 1 and y2 <= y1 + 1:
    print("Legal move")

else:
    print("Illegal move")