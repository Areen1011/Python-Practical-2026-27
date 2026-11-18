roll = (101, 102, 103, 104, 105)

print("Tuple:", roll)
print("First Element:", roll[0])
print("Last Element:", roll[-1])
print("Slicing:", roll[1:4])
print("Concatenation:", roll + (106, 107))

a = {101, 102, 103, 104}
b = {103, 104, 105, 106}

print("Set A:", sorted(a))
print("Set B:", sorted(b))

print("Union:", sorted(a | b))
print("Intersection:", sorted(a & b))
print("Difference:", sorted(a - b))
print("Symmetric Difference:", sorted(a ^ b))

print("Subset:", a.issubset(b))
print("Superset:", a.issuperset(b))

a.add(107)
print("After Add:", sorted(a))

a.remove(101)
print("After Remove:", sorted(a))

n = int(input("Enter range: "))
squares = {x * x for x in range(1, n + 1) if x % 2 == 0}

print("Squares of Even Numbers:", sorted(squares))
