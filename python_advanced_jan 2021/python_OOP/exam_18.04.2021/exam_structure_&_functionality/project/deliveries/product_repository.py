from project.deliveries.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        product_names = [p.name for p in self.products]
        if product.name in product_names:
            raise ValueError(f"Product {product.name} already exists.")
        self.products.append(product)
        return f"Product {product.name} successfully added to inventory."

    def decrease(self, product: Product, quantity: int):
        if product in self.products:
            product.quantity -= quantity
            return f"Left quantity of {product.name}: {product.quantity}"

    def find(self, product_name: str):
        filtered_products = [p for p in self.products if p.name == product_name]
        if filtered_products:
            product = filtered_products[0]
            return product
        else:
            return "None"
