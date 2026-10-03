credits = (4, 3, 4, 2, 3, 4)
print("Credit hours:", credits)

total = sum(credits)
average = total / len(credits)

print("Total credit hours:", total)
print("Average credit hours:", average)

maximum = max(credits)
minimum = min(credits)

print("Maximum credit hours:", maximum)
print("Minimum credit hours:", minimum)

search = int(input("Enter credit value to search: "))

if search in credits:
    print(search, "credit hours are present.")
else:
    print(search, "credit hours are not present.")

count = credits.count(search)
print("Number of courses with", search, "credit hours:", count)

additional = (3, 2)
new_credits = credits + additional

print("After adding two courses:", new_credits)

repeated = credits * 2
print("Original tuple repeated twice:", repeated)

first_three = credits[:3]
print("First three credit values:", first_three)