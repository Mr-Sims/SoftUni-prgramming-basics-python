from project.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"


# kitteh = Cat("Chancho", 5, "FAT male")
#
# print(kitteh)
# print(kitteh.make_sound())