from project.animals.animal import Bird
from project.food import Vegetable
from project.food import Seed
from project.food import Meat
from project.food import Fruit


class Owl(Bird):
    pass
    # def __init__(self, name, weight, wing_size, food_eaten=0):
    #     super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        no_eat = ["Fruit", "Vegetable", "Seed"]
        if food.__class__.__name__ in no_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.25



class Hen(Bird):
    pass
    # def __init__(self, name, weight, wing_size, food_eaten=0):
    #     super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35




owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)