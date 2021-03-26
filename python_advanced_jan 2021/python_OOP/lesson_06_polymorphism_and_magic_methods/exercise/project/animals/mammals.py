from project.animals.animal import Mammal
from project.food import Vegetable
from project.food import Seed
from project.food import Meat
from project.food import Fruit


class Mouse(Mammal):
    pass

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        no_eat = ["Meat", "Seed"]
        if food.__class__.__name__ in no_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.10
        return


class Dog(Mammal):
    pass

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        no_eat = ["Fruit", "Seed", "Vegetable"]
        if food.__class__.__name__ in no_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.40
        return


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        no_eat = ["Fruit", "Seed"]
        if food.__class__.__name__ in no_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.30
        return


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 1.00
        return


# tiger = Tiger("Shirhan", 500, "India")
# print(tiger)
# meat = Meat(4)
# print(tiger.make_sound())
# tiger.feed(meat)
# veg = Vegetable(1)
# print(tiger.feed(veg))
# print(tiger)