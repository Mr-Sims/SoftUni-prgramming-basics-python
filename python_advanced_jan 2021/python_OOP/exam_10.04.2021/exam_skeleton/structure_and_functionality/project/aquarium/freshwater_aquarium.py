from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.base_fish import BaseFish
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):
    initial_capacity = 50

    def __init__(self, name: str):
        super().__init__(name, self.initial_capacity)

    # def add_fish(self, fish):
    #     if fish.__class__.__name__ == "FreshwaterFish" and self.current_capacity > 0:
    #         self.fish.append(fish)
    #         self.current_capacity -= 1
    #         return f"Successfully added {fish.__class__.__name__} to {self.name}."
    #     if self.current_capacity <= 0:
    #         return f"Not enough capacity"

