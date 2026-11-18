name = input("Enter full name: ")
email = input("Enter email: ")
mobile = input("Enter mobile number: ")

first = name[:name.index(" ")]
last = name[name.rindex(" ") + 1:]

print("First Name:", first)
print("Last Name:", last)
print("Reversed Name:", name[::-1])

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)

print("Last Four Digits:", mobile[-4:])

print("\nStudent Information")
print(f"Name: {name}")
print("Email: {}".format(email))
print("Mobile: %s" % mobile)

print("First Character:", name[0])
print("Last Character:", name[-1])
