from project.deliveries.product import Product


class Food(Product):
    initial_quantity = 15

    def __init__(self, name, quantity=initial_quantity):
        super().__init__(name, quantity)


# parjola = Food("VratnaParjola", 0)
#
# print(parjola.__dict__)
