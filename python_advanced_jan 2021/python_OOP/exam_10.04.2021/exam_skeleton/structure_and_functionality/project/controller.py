from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_types:
            return "Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}"
        if aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}"

    def add_decoration(self, decoration_type: str):
        valid_types = ["Ornament", "Plant"]
        if decoration_type not in valid_types:
            return "Invalid decoration type."

        if decoration_type == "Plant":
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}"
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}"

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

        decoration = [x for x in self.decorations_repository.decorations if x.__class__.__name__ == decoration_type]
        if not decoration:
            return f"There isn't a decoration type {decoration_type}"

        if aquarium:
            if aquarium in self.aquariums:
                aquarium.add_decoration(decoration)
                self.decorations_repository.decorations.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}"

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}"

        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        if aquarium.__class__.__name__ == "FreshwaterAquarium" and fish_type == "SaltwaterFish":
            return "Water not suitable"
        if aquarium.__class__.__name__ == "SaltwaterAquarium" and fish_type == "FreshwaterFish":
            return "Water not suitable"
        if aquarium.current_capacity <= 0:
            return "Not enough capacity"

        if fish_type == "SaltwaterFish":
            aquarium.add_fish(SaltwaterFish(fish_name, fish_species, price))
            return f"Successfully added {fish_type} to {aquarium_name}"
        if fish_type == "FreshwaterFish":
            aquarium.add_fish(FreshwaterFish(fish_name, fish_species, price))
            return f"Successfully added {fish_type} to {aquarium_name}"

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        fishes_value = sum([fish.price for fish in aquarium.fish])
        decorations_value = sum([decoration.price for decoration in aquarium.decorations])
        total = fishes_value + decorations_value
        return f"The value of Aquarium {aquarium_name} is {total:.2f}"

    def report(self):
        pass
