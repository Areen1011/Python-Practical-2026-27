cart = []

for i in range(5):
    add_item = input(f"Enter product {i+1} to add to the cart: ")
    cart.append(add_item)

print("Current shopping cart:", cart)

print("Total items in cart:", len(cart))