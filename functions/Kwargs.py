def kwargs_demo(**kwargs):
    print(kwargs, type(kwargs))


print(kwargs_demo(a = "one", b = "two")) # takes keyword arguments and converts them to a dictionary


def calculate_tip(list_of_meals, total_cost, tip_pc):
    print("You had:")
    for meal in list_of_meals:
        print(meal)
    print(f"Your subtotal is: {total_cost}")
    print(f"With a {tip_pc:.0%} tip, the total is £{total_cost * (1 + tip_pc):.2f}")


calculate_tip(["burger", "pizza"], 18.50, 0.1)

calculate_tip(
    list_of_meals=["hot dog", "chips"],
    tip_pc=0.15,
    total_cost=24
)


def calculate_total_cost(**meal_prices):
    print(meal_prices, type(meal_prices))
    total = 0
    for price in meal_prices.values():
        total += price
    return total
#sum(meal_prices.values()) will also work

print(calculate_total_cost(
    Pizza=10.50,
    Burger=9.00,
    HotDog=5.50
))