##########################################################
### solution 100/100 - no funcs, hardly any comprehensions, dict + lists



hero_names = input().split(", ")
hero_dict = {hero: [[], 0] for hero in hero_names}
line = input()

while not line == "End":
    hero, item, cost = line.split("-")
    cost = int(cost)
    if item not in hero_dict[hero][0]:
        hero_dict[hero][0].append(item)
        hero_dict[hero][1] += cost
    line = input()

print(*[f'{key} -> Items: {len(value[0])}, Cost: {value[1]}' for key, value in hero_dict.items()], sep="\n")

#######################################################################################################
######################################################################################################
#### solution nested dict


def update_heroes(name, item, price, heroes):

    if not heroes.get(name):
        heroes[name] = {}
    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})
    return heroes


names = input().split(", ")

data = input()
heroes = {name: {} for name in names}

while not data == "End":
    name, item, price = data.split("-")
    heroes = update_heroes(name, item, price, heroes)

    data = input()

print(*[f'{name} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}' for name, inventory in heroes.items()], sep="\n")
