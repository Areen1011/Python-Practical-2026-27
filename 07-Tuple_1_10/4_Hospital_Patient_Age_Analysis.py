age = (25, 32, 18, 45, 29, 32, 52, 19, 40, 32)
print("Patient ages:", age)

average = sum(age) / len(age)
print("Average age:", average)

oldest = max(age)
youngest = min(age)

print("Oldest patient:", oldest)
print("Youngest patient:", youngest)

ages = int(input("Enter age to count: "))
count = age.count(ages)
print("Number of patients aged", ages, ":", count)

search = int(input("Enter age to search: "))

if search in age:
    print("Age", search, "is present.")
else:
    print("Age", search, "is not present.")

start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

print("Patient ages in specified range:", age[start:end])

if all(age > 18 for age in age):
    print("All patients are above 18 years.")
else:
    print("Not all patients are above 18 years.")