###################################################################################
######################## Решение от LAB-a  ##################################################


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "birds":
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes: {', '.join(self.fishes)}\n"
#         elif species == "birds":
#             result += f"Birds: {', '.join(self.birds)}\n"
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
#
# for i in range(count):
#     animal = input().split()
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))


#####################################################################
###############################  Решение Дончо  ######################################
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.birds = []
#         self.mammals = []
#         self.fish = []
#
#     def get_animals_by_species(self, species):
#         animals = []
#         if species == "mammal":
#             animals = self.mammals
#         elif species == "bird":
#             animals = self.birds
#         elif species == "fish":
#             animals = self.fish
#         return animals
#
#     def add_animal(self, species, animal):
#         animals = self.get_animals_by_species(species)
#         animals.append(animal)
#         self.__animals += 1
#
#     def get_info(self, species):
#         animals = self.get_animals_by_species(species)
#         print(f"Mammals in Great Zoo: {', '.join(animals)}")
#         print(f"Total animals: {self.__animals}")
#
#
# zoo = Zoo(input())
#
# animals_count = int(input())
#
# for _ in range(animals_count):
#     [species, animal] = input().split()
#     zoo.add_animal(species, animal)
#
# species = input()
# zoo.get_info(species)


##########################################################################################
#################################### Решение от DISCORD-a ###############################################



# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.births = []
#
#     def add_animals(self, species, names):
#         if species == "mammal":
#             self.mammals.append(names)
#         elif species == "fish":
#             self.fishes.append(names)
#         elif species == "bird":
#             self.births.append(names)
#         Zoo.__animals += 1
#
#     def get_info(self, info):
#         result = ''
#         if info == "mammal":
#             result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif info == "fish":
#             result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif info == "birth":
#             result = f"Birds in {self.name}: {', '.join(self.births)}\n"
#         return result + f'Total animals: {Zoo.__animals}'
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# number = int(input())
#
# for _ in range(number):
#     line = input()
#     species, name = line.split()
#     zoo.add_animals(species, name)
#
# info = input()
# print(zoo.get_info(info))

#############################################################################################################
#############################################################################################################
################################# Решение ИНЕС ################################################################


class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)
        Zoo.__animals += 1

    def get_info(self, species):

        animals_to_display = []
        if species == "mammal":
            animals_to_display = self.mammals
        elif species == "fish":
            animals_to_display = self.fishes
        elif species == "bird":
            animals_to_display = self.birds
        species = species.capitalize() + "es" if species == "fish" else species.capitalize() + "s"
        return f"{species} in {self.name}: {', '.join(animals_to_display)}\nTotal animals: {Zoo.__animals}"

zoo_name = input()
rows_n = int(input())

zoo = Zoo(zoo_name)

for i in range(rows_n):
    species, animal_name = input().split()
    zoo.add_animal(species, animal_name)


req_species = input()

print(zoo.get_info(req_species))