booked_seats = (5, 12, 18, 25, 32, 40, 45)
print("Booked seats:", booked_seats)

seat = int(input("Enter seat number to check: "))

if seat in booked_seats:
    print("Seat", seat, "is booked.")
else:
    print("Seat", seat, "is not booked.")

print("First booked seat:", booked_seats[0])
print("Last booked seat:", booked_seats[-1])

print("Total booked seats:", len(booked_seats))

start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

print("Seats in specified range:", booked_seats[start:end])

print("Booked seats in reverse order:", booked_seats[::-1])