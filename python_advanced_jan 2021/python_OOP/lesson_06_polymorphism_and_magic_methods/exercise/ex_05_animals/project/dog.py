from project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"


# doge = Dog("Charlie", 5, "male")
#
# print(doge)
# print(doge.make_sound())