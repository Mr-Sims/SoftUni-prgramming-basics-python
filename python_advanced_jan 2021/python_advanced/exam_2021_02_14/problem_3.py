def stock_availability(inventory_list, *commands):
    command = commands[0]
    if command == "delivery":
        for el in commands[1:]:
            inventory_list.append(el)
    elif command == "sell":
        if commands[1:]:
            for el in commands[1:]:
                if isinstance(el, int):
                    for i in range(int(el)):
                        inventory_list.pop(0)
                else:
                    if el in inventory_list:
                        inventory_list = [x for x in inventory_list if not x == el]
        else:
            inventory_list.pop(0)
    return inventory_list

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


