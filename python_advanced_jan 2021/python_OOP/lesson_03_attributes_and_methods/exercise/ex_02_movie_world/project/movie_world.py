class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):

        # for customer in self.customers:
        #     print(customer)
        # for dvd in self.dvds:
        #     print(dvd)
        res = '\n'.join([c.__repr__() for c in self.customers])
        res += '\n' + '\n'.join([d.__repr__() for d in self.dvds])
        return res

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def get_customer_by_customer_id(self, customer_id):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        return customer

    def get_dvd_by_dvd_id(self, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        return dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.get_customer_by_customer_id(customer_id)
        dvd = self.get_dvd_by_dvd_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        customer.rented_dvds_by_name.append(dvd.name)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self.get_customer_by_customer_id(customer_id)
        dvd = self.get_dvd_by_dvd_id(dvd_id)
        if dvd.name in customer.rented_dvds_by_name:
            customer.rented_dvds.remove(dvd)
            customer.rented_dvds_by_name.remove(dvd.name)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

