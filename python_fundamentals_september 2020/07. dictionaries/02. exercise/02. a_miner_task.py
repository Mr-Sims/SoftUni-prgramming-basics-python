inventory = {}

while True:
    line = input()

    if line == "stop":
        break

    key = line
    value = int(input())
    if key not in inventory:
        inventory[key] = value
    else:
        inventory[key] += value


for key, value in inventory.items():
    print(f"{key} -> {value}")
