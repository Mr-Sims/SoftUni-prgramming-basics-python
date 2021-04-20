from project.sales.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.customers = []   # will contain all customers

    def add(self, customer: Customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")
        return self.customers.append(customer)

    def remove(self, customer_name: str):
        filtered_customers = [c for c in self.customers if c.name == customer_name]
        if not filtered_customers:
            raise ValueError(f"Customer {customer_name} does not exist.")
        customer = filtered_customers[0]
        self.customers.remove(customer)
        return f"Removed customer: {customer_name}"

    def find(self, customer_name: str):
        filtered_customers = [c for c in self.customers if c.name == customer_name]
        if not filtered_customers:
            return "None"
        customer = filtered_customers[0]
        return customer
