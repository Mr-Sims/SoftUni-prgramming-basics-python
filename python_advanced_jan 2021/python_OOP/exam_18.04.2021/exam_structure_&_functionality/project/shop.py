from project.deliveries.product import Product
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository
from project.deliveries.product_repository import ProductRepository
from project.deliveries.food import Food
from project.deliveries.drink import Drink


class Shop:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        product = None
        if product_type == "Drink":
            return self.product_repository.add(Drink(name))
        elif product_type == "Food":
            return self.product_repository.add(Food(name))

# method sell version 1:
    def customer_create_or_find(self, customer_name):
        if self.customer_repository.find(customer_name) == "None":
            self.customer_repository.add(Customer(customer_name))
            customer = [c for c in self.customer_repository.customers if c.name == customer_name][0]
        else:
            customer = self.customer_repository.find(customer_name)
        return customer

    def sell(self, customer_name: str, **shopping_list):
        res = ""
        customer = self.customer_create_or_find(customer_name)
        for item, quantity in shopping_list.items():
            product = self.product_repository.find(item)
            if product.quantity > shopping_list[item]:
                res += self.product_repository.decrease(product, shopping_list[item])
                res += "\n"
                customer.products[item] = quantity
            else:
                res += f"Left quantity of {product.name}: 0\n"
                customer.products[item] = product.quantity
                self.product_repository.products.remove(product)
        return res


# method sell version 2:
#     def sell(self, customer_name: str, **shopping_list):
#         bought_products_left_quantities = {}
#         customer = self.customer_repository.find(customer_name)
#         if customer == "None":
#             customer = self.customer_repository.add(Customer(customer_name))
#         customer = [c for c in self.customer_repository.customers if c.name == customer_name][0]
#         item_names = [i.name for i in self.product_repository.products]
#
#         for item, quantity in shopping_list.items():
#
#             if item in item_names:
#                 item_in_shop = [i for i in self.product_repository.products if i.name == item][0]
#                 if item_in_shop.quantity > quantity:
#
#
#                     item_in_shop.quantity -= quantity
#                     customer.products[item] = quantity
#
#                     bought_products_left_quantities[item] = item_in_shop.quantity
#
#                 elif item_in_shop.quantity <= quantity:
#                     customer.products[item] = item_in_shop.quantity
#                     self.product_repository.products.remove(item_in_shop)
#                     bought_products_left_quantities[item] = 0
#
#         ll = []
#         for key, value in bought_products_left_quantities.items():
#             ll.append(key)
#         last_item = ll[-1]
#         res = ""
#         for item, quantity in bought_products_left_quantities.items():
#             if not item == last_item:
#                 res += f"Left quantity of product {item}: {quantity}\n"
#             else:
#                 res += f"Left quantity of product {item}: {quantity}"
#         return res


   # # version 3
    # def sell(self, customer_name: str, **shopping_list):
    # res = ""
    # if self.customer_repository.find(customer_name) == "None":
    #     self.customer_repository.add(Customer(customer_name))
    #     customer = [c for c in self.customer_repository.customers if c.name == customer_name][0]
    # else:
    #     customer = self.customer_repository.find(customer_name)
    # for item, quantity in shopping_list.items():
    #     product = self.product_repository.find(item)
    #     try:
    #         res += self.product_repository.decrease(product, shopping_list[item])
    #         res += "\n"
    #         customer.products[item] = quantity
    #     except ValueError:
    #         customer.products[item] = quantity
    #         res += f"Left quantity of {product.name}: 0\n"
    #         self.product_repository.products.remove(product)
    # return res