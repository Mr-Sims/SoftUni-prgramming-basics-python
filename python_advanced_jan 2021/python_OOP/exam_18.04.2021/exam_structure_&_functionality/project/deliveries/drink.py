from project.deliveries.product import Product


class Drink(Product):
    initial_quantity = 10

    def __init__(self, name: str, quantity=initial_quantity):
        super().__init__(name, quantity)



