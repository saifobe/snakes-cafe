print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

for item in menu:
    print(item)
    print("-" * len(item))
    for i in menu[item]:
        print(i)
    print("")

print("""
***********************************
** What would you like to order? **
***********************************
""")

orders = {}
while True:
        order = input("> ")
        if order == "quit" or order == "Quit":
            print("Thanks for visiting Snakes cafe.")
            break
        elif order in orders:
            orders[order] += 1
        elif order in [item for sublist in menu.values() for item in sublist]:
            orders[order] = 1
        else:
            print("Sorry, We Don't Have Your Order in Our Menu.")
        print(f"\n** {orders[order]} order{'s' if orders[order] > 1 else ''} of {order} have been added to your meal **\n")
        


     

