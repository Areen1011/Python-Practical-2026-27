x = 10

def display():
    global x
    x = 20
    y = 5
    print("Global variable:", x)
    print("Local variable:", y)

display()

print("Global variable outside function:", x)

square = lambda a: a * a
cube = lambda a: a * a * a
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

print("Square:", square(5))
print("Cube:", cube(3))
print("Maximum:", maximum(10, 20))
print("Addition:", addition(10, 20))
