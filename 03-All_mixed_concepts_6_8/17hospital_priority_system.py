critical = input("Is patient critical? (yes/no): ")
senior = input("Is patient a senior citizen? (yes/no): ")
child = input("Is patient a child? (yes/no): ")
pregnant = input("Is patient pregnant? (yes/no): ")

if critical == "yes":
    print("Priority 1 - Critical Patient")

elif senior == "yes" or pregnant == "yes":
    print("Priority 2 - High Priority")

elif child == "yes":
    print("Priority 3 - Child")

else:
    print("Priority 4 - General Patient")