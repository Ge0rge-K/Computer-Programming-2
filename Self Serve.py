menu_items = ["Burger", "Fries", "Medium Soda", "Salad", "Ice Cream", "Chicken Tenders", "Large Soda", "Milk Shake"]
menu_prices = [5.99, 2.99, 1.50, 4.25, 3.75, 5.99, 2.50, 3.50]

# User order
order = []
order_total = 0.0

def display_menu():
    print("\n--- Welcome to the Shake Shack! ---")
    for i in range(len(menu_items)):
        print(f"{i + 1}. {menu_items[i]} - ${menu_prices[i]:.2f}")
    print("0. Finish order and checkout")

def add_to_order(choice):
    global order_total
    item_index = choice - 1
    order.append(menu_items[item_index])
    order_total += menu_prices[item_index]
    print(f"Added {menu_items[item_index]} to your order. Current total: ${order_total:.2f}")

def checkout():
    print("\n--- Your Order ---")
    for item in order:
        print(f"- {item}")
    print(f"Total: ${order_total:.2f}")
    
    print("Swipe card or insert cash.")
    card_swipe = input("Swipe Card? (Y/N): ").strip().upper()

    if card_swipe == "Y":
        print("Processing card payment...")
        print("Payment approved! Thank you for your order!")
    elif card_swipe == "N":
        try:
            cash = float(input("Enter cash amount: $"))
            if cash >= order_total:
                change = cash - order_total
                print(f"Payment accepted. Your change is ${change:.2f}.")
                print("Thank you for your order!")
            else:
                print("Insufficient cash. Transaction cancelled.")
        except ValueError:
            print("Invalid input. Transaction cancelled.")
    else:
        print("Invalid input. Transaction cancelled.")

# Main loop
while True:
    display_menu()
    try:
        choice = int(input("Select an item by number (0 to checkout): "))
        if choice == 0:
            checkout()
            break
        elif 1 <= choice <= len(menu_items):
            add_to_order(choice)
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
