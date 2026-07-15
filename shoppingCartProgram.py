# Shopping Cart Program

items = []
prices = []
total = 0

while True:
    item = input("Enter an item to in your cart (q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {item}: $"))
        items.append(item)
        prices.append(price)

print()
print("----- YOUR CART -----")
print()

for item in items:
    print(item)

for price in prices:
    total += price

print()
print(f"Your total is: ${total:.2f}")
