# Shopping Cart Program

# Ask user how many items
num_items = int(input("How many items do you want to add? "))

# Lists to store items and prices
items = []
prices = []

# Input each item
for i in range(num_items):
    name = input(f"Enter name of item {i+1}: ")
    price = float(input(f"Enter price of {name}: RM "))
    items.append(name)
    prices.append(price)

# Print receipt
print("\n--- Shopping Cart ---")
total = 0
for i in range(num_items):
    print(f"{i+1}. {items[i]} - RM {prices[i]:.2f}")
    total += prices[i]

print(f"Total = RM {total:.2f}")
