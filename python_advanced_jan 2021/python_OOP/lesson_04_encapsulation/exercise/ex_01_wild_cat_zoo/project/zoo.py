class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def check_if_animal_capacity(self):
        return self.__animal_capacity > 0

    def check_if_budget(self, price):
        return self.__budget >= price

    def add_animal(self, animal, price):
        if self.check_if_budget(price) and self.check_if_animal_capacity():
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.check_if_animal_capacity() and not self.check_if_budget(price):
            return f"Not enough budget"
        elif not self.check_if_animal_capacity() and self.check_if_budget(price):
            return "Not enough space for animal"

    def check_if_worker_capacity(self):
        return self.__workers_capacity > len(self.workers)

    def hire_worker(self, worker):
        if self.check_if_worker_capacity():
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def get_worker_by_name(self, worker_name):
        try:
            worker = [worker for worker in self.workers if worker_name == worker.name][0]
            return worker
        except:
            return None

    def fire_worker(self, worker_name):
        if self.get_worker_by_name(worker_name) == None:
            return f"There is no {worker_name} in the zoo"
        worker = self.get_worker_by_name(worker_name)
        self.workers.remove(worker)
        self.__workers_capacity += 1
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_expenses = 0
        for animal in self.animals:
            animal_expenses += animal.get_needs()
        if animal_expenses <= self.__budget:
            self.__budget -= animal_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        tigers = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        lions = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == "Lion"]
        cheetahs = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion
            result += "\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger
            result += "\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += cheetah
            if cheetah != cheetahs[-1]:
                result += "\n"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper
            result += "\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker
            result += "\n"

        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += vet
            if vet != vets[-1]:
                result += "\n"
        return result
