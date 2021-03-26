from project.cat import Cat

class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.GENDER)

    def make_sound(self):
        return "Hiss"

#
# kitteh = Tomcat("Chancho", 5)
#
# print(kitteh)
# print(kitteh.make_sound())