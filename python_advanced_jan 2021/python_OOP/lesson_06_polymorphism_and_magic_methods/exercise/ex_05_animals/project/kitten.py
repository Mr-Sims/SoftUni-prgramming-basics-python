from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.GENDER)
        #self.gender = "Female"

    def make_sound(self):
        return "Meow"



# kitteh = Kitten("Chancho", 5)
#
# print(kitteh)
# print(kitteh.make_sound())