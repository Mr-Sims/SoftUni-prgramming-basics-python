from project.deliveries.product import Product
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository
from project.deliveries.product_repository import ProductRepository
from project.deliveries.food import Food
from project.deliveries.drink import Drink
from project.shop import Shop

peter = Customer("Peter")


shop = Shop()
shop.customer_repository.add(peter)

shop.deliver("Drink", "Tea")
shop.deliver("Drink", "Coffee")
shop.deliver("Food", "Steak")
shop.deliver("Food", "Butter")
shop.deliver("Food", "Bread")

shoping_list = {

    "Tea": 10,
    "Coffee": 8,
    "Steak": 15,
    "Butter": 8,
}
print(shop.sell("Peter", **shoping_list))
a = 5


# shop = Shop()
# print(shop.deliver('Food', 'eggs'))
# print(shop.deliver('Food', 'bread'))
# print(shop.deliver('Drink', 'water'))
# print(shop.deliver('Drink', 'milk'))
# customer = Customer('George')
# print(shop.customer_repository.add(customer))
# print(shop.sell('George', **{'bread': 10, 'eggs': 8, 'water': 20, 'milk': 5, 'cola': 18}))
# print(customer.name)
# print([c.products for c in shop.customer_repository.customers])