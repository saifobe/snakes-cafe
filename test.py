menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

orders = {}

def print_menu():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**                                  **")
    print("** To quit at any time, type 'quit' **")
    print("**************************************")

    for category, items in menu.items():
        print("\n" + category)
        print("-" * len(category))
        for item in items:
            print(item)

    print("\n" + "*" * 35)
    print("** What would you like to order? **")
    print("*" * 35)

def take_order():
    while True:
        order = input("> ")
        if order == "quit":
            break
        elif order in orders:
            orders[order] += 1
        elif order in [item for sublist in menu.values() for item in sublist]:
            orders[order] = 1
        else:
            print("Sorry, that item is not on the menu.")
        print(f"\n** {orders[order]} order{'s' if orders[order] > 1 else ''} of {order} have been added to your meal **\n")
    print("Exiting")

def print_summary():
    print("\n" + "*" * 35)
    print("Here is your complete order:")
    for item, count in orders.items():
        print(f"{count} order{'s' if count > 1 else ''} of {item}")
    print("*" * 35)

if __name__ == "__main__":
    print_menu()
    take_order()
    print_summary()
