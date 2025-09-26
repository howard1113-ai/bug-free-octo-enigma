def add_expenses():
    print("Enter your expenses (type 'q' to stop):")
    while True:
        item = input("Item name: ")
        if item.lower() == "q":
            break
        
        price = input("Price (per item): ")
        if price.lower() == "q":
            break
        
        quantity = input("Quantity: ")
        if quantity.lower() == "q":
            break

        # Save to file (item, price, quantity)
        with open("expenses.txt", "a") as f:
            f.write(f"{item},{price},{quantity}\n")


def show_expenses():
    total = 0
    print("\n--- Expenses ---")
    
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                item, price, quantity = line.strip().split(",")
                price = float(price)
                quantity = int(quantity)
                cost = price * quantity
                print(f"{item} x {quantity} - RM {cost:.2f}")
                total += cost
    except FileNotFoundError:
        print("No expenses found.")

    print(f"Total = RM {total:.2f}")


def main():
    add_expenses()
    show_expenses()


if __name__ == "__main__":
    main()

