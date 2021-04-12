from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish
from project.decoration.base_decoration import BaseDecoration
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament

class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []
        self.current_capacity = capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = sum([x.comfort for x in self.decorations])
        return total_comfort

    # @abstractmethod
    def add_fish(self, fish):
        if self.current_capacity <= 0:
            return "Not enough capacity."
        self.fish.append(fish)
        self.current_capacity -= 1
        return f"Successfully added {fish.__class__.__name__} to {self.name}"

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = [fish.name for fish in self.fish]
        res = f"{self.name}:\nFish: "
        if fish_names:
            res += ', '.join(fish_names)

        else:
            res += "none\n"
        res += f"\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}\n"
        return res



