menu_file = open("menu.txt")
items = list(map(lambda x: x.strip(), menu_file.readlines()))
menu = dict(i.split(',') for i in items)
menu_file.close()


def grab_orders() -> dict:
    orders = open("orders.txt")
    lines = orders.read().split("\n")
    orders.close()

    all_orders = []
    for the_order in lines:
        if len(the_order) > 0:
            this_order = {}
            items = the_order.split(',')
            for item in items:
                if len(item) > 0:
                    drink_name, price, qty = item.split(':')
                    this_order[drink_name] = [price, qty]
            all_orders.append(this_order)
    return all_orders


def display_order(the_order: dict):
    print("\nYour order:")
    total = 0
    for the_drink in the_order.keys():
        sub = float(the_order[the_drink][0]) * int(the_order[the_drink][1])
        total += sub
        print(f"    {the_order[the_drink][1]} {the_drink}: £{sub:.2f}")
    print(f"Total £{total:.2f}")


def add_to_order(the_order, the_drink):
    if the_drink in the_order:
        the_order[the_drink][1] += 1
    else:
        drink_price = menu[the_drink]
        the_order[the_drink] = [drink_price, 1]


def take_order():
    pass
    print("")
    order = {}

    while True:
        user = input("Select drink or q to confirm order: ")
        if user == 'q':
            if len(order) > 0:
                display_order(order)
                user = input("Confirm (y) or cancel: ")
                if user == 'y':
                    return order
                else:
                    return None
            else:
                return None

        elif user in menu:
            add_to_order(order, user)
        else:
            raise ValueError

        # get input
        # if input q
            # if order not empty
                # display order (drinks and prices)
                # get input - confirm order or cancel
                # if input confirm
                    # return order
                # else
                    # return blank
            # else (order empty)
                # return blank
        # else
            # if valid drink_name
                # add to order
            # else
                # throw error

# order dictionary key - drink_name, value (price, qty)


while True:
    user_selection = input("\n\n\nPlace order (o) or view orders (v): ")
    if user_selection == 'o':
        print('\n\n\n----MENU----')
        for drink in menu.keys():
            print(f'    {drink} £{float(menu[drink]):.2f}')

        order = take_order()
        if order is not None:
            order_str = ""
            for drink in order:
                order_str += f"{drink}:{order[drink][0]}:{order[drink][1]},"
            order_file = open("orders.txt", 'a')
            order_file.write(f"{order_str}\n")
            order_file.close()

    elif user_selection == 'v':
        orders = grab_orders()
        for this_order in orders:
            display_order(this_order)
            print("")

    else:
        print("Enter valid selection")
