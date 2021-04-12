from project.aquarium.base_aquarium import BaseAquarium
from project.fish.base_fish import BaseFish
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament

class SaltwaterAquarium(BaseAquarium):
    initial_capacity = 25

    def __init__(self, name: str):
        super().__init__(name, self.initial_capacity)

    # def add_fish(self, fish):
    #     if fish.__class__.__name__ == "SaltwaterFish" and self.current_capacity > 0:
    #         self.fish.append(fish)
    #         self.current_capacity -= 1
    #         return f"Successfully added {fish.__class__.__name__} to {self.name}."
    #     if self.current_capacity <= 0:
    #         return f"Not enough capacity"
#
# sharky = SaltwaterFish("Sharky", "shark", 500)
# sharky2 = SaltwaterFish("Sharky2", "shark", 500)
#
# salty = SaltwaterAquarium("Salty")
#
# salty.add_fish(sharky)
# salty.add_fish(sharky2)
#
# salty.feed()
#
# sharanko = FreshwaterFish("Sharo", "sharan", 6)
# salty.add_fish(sharanko)
# plant = Plant()
# plant2 = Plant()
# salty.add_decoration(plant)
# salty.add_decoration(plant2)
#
# print(salty.__str__())