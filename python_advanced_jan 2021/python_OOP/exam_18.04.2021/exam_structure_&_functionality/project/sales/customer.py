class Customer:
    def __init__(self, name: str):
        self.name = name
        self.products = {}


    ### products: dict[str, int] - empty dictionary upon initialization
    # that will contain all bought product's names as key argument
    # and bought quantity as value argument.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The customer's name cannot be an empty string.")
        self.__name = value
