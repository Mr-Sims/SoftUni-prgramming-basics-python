product = input()
units = int(input())


def order(prod, qnty):
    price = None
    if prod == "coffee":
        price = qnty * 1.5
    elif prod == "water":
        price = qnty * 1.00
    elif prod == "coke":
        price = qnty * 1.4
    elif prod == "snacks":
        price = qnty * 2.00
    return (price)


print(f"{order(product, units):.2f}")