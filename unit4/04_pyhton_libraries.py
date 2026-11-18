import math
import random
from datetime import datetime, date


n = int(input("Enter a number: "))

print("Square Root:", math.sqrt(n))
print("Factorial:", math.factorial(n))
print("Power:", math.pow(n, 2))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.3))


print("Random Integer:", random.randint(1, 100))

lst = [10, 20, 30, 40, 50]

print("Original List:", lst)
print("Random Element:", random.choice(lst))

random.shuffle(lst)
print("Shuffled List:", lst)


today = datetime.now()

print("Current Date and Time:", today)
print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

d1 = date(2026, 1, 1)
d2 = date(2026, 11, 18)

diff = d2 - d1

print("First Date:", d1)
print("Second Date:", d2)
print("Difference in Days:", diff.days)
