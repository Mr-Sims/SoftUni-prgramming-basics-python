inventory = input().split(", ")
data = input()


def collect(inv, i):
    if i not in inventory:
        inv.append(i)
    return inv


def drop(inv, i):
    if i in inv:
        inv.remove(i)
    return inv


def combine(inv, i):
    old_item, new_item = i.split(":")

    if old_item in inv:
        #index_old_item = inv.index(old_item)
        index_new_item = inv.index(old_item) + 1
        inv.insert(index_new_item, new_item)
    return inv


def renew(inv, i):
    if i in inv:
        inv.remove(i)
        inv.append(i)
    return inv


while data != "Craft!":
    command, item = data.split(" - ")

    if command == "Collect":
        inventory = collect(inventory, item)
    elif command == "Drop":
        inventory = drop(inventory, item)
    elif command == "Combine Items":
        inventory = combine(inventory, item)
    elif command == "Renew":
        inventory = renew(inventory, item)


    data = input()

print(", ".join(inventory))