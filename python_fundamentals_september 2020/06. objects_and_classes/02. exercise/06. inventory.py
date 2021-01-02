class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        self.item = item
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = len(self.items) - self.__capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
