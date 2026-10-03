marks = (70,50,60,80,90)

print("Total ", sum(marks))

percentage = sum(marks) / len(marks)

print("Percentage ",  percentage)

print("Minimum ",min(marks))
print("Maximum", max(marks))

passed = (mark >= 40 for mark in marks)

if passed:
    print("Result: Passed in all subjects")
else:
    print("Result: Failed in one or more subjects")

print(marks[::-1])