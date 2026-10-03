sales = (120, 250, 180, 250, 100)
print("Sales quantities:", sales)

total = sum(sales)
print("Total sales:", total)

average = total / len(sales)
print("Average sales:", average)

highest = max(sales)
lowest = min(sales)

print("Highest sales:", highest)
print("Lowest sales:", lowest)

search = int(input("Enter sales quantity to search: "))

if search in sales:
    print(search, "is present in the sales tuple.")
else:
    print(search, "is not present in the sales tuple.")

count = sales.count(search)
print("Occurrences of", search, ":", count)

descending = tuple(sorted(sales, reverse=True))
print("Sales in descending order:", descending)