treasure_chest = input().split("|")
stolen_items_list = []

while True:

    line = input()
    if line == "Yohoho!":
        break

    if line.split()[0] == "Loot":
        loot_list = (line.split())
        loot_list.remove(loot_list[0])
        for item in loot_list:
            if item in treasure_chest:
                continue
            else:
                treasure_chest.insert(0, item)
    elif line.split()[0] == "Drop":
        index = int(line.split()[1])
        if index >= (len(treasure_chest)) -1:
            continue
        else:
            treasure_chest.append(treasure_chest.pop(index))

    elif line.split()[0] == "Steal":
        items_to_steal = int(line.split()[1])
        if items_to_steal  <= (len(treasure_chest)):
            stolen_items_list = treasure_chest[len(treasure_chest) - items_to_steal:]
            treasure_chest = treasure_chest[:len(treasure_chest) - items_to_steal]
            res = ', '.join(stolen_items_list)
            print(res)
        else:
            stolen_items_list = treasure_chest.copy()
            treasure_chest = []
            res = ", ".join(stolen_items_list)
            print(res)

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    suma = 0
    for item in range(len(treasure_chest)):
        suma += len(treasure_chest[item])
    print(f"Average treasure gain: {suma / len(treasure_chest):.2f} pirate credits.")