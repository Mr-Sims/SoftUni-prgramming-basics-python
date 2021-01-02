#########################   Мое Решение  ####################################################

grocery_list = input().split("!")


def item_is_in(product):
    if product in grocery_list:
        return True


while True:
    line = input()
    if line == "Go Shopping!":
        break
    if "Correct" in line:
        command, item, item_2 = line.split()
        if item_is_in(item):
            item_index = grocery_list.index(item)
            grocery_list.remove(item)
            grocery_list.insert(item_index, item_2)
    else:
        command, item, = line.split()
        if command == "Urgent":
            if not item_is_in(item):
                grocery_list.insert(0, item)
        elif command == "Unnecessary":
            if item_is_in(item):
                grocery_list.remove(item)
        elif command == "Rearrange":
            if item_is_in(item):
                grocery_list.remove(item)
                grocery_list.append(item)
print(", ".join(grocery_list))


#########################   Инес Решение  ####################################################

# items = input().split("!")
# command = input()
#
#
# def checkItem_exists(items_list, item_searched):
#     return True if item_searched in items_list else False
#
#
# while not command == "Go Shopping!":
#     command_type = command.split()[0]
#     item = command.split()[1]
#     if command_type == "Urgent":
#         if not checkItem_exists(items, item):
#             items.insert(0, item)
#     elif command_type == "Unnecessary":
#         if checkItem_exists(items, item):
#             items.remove(item)
#     elif command_type == "Correct":
#         if checkItem_exists(items, item):
#             new_item = command.split()[2]
#             currents_index = items.index(item)
#             items[currents_index] = new_item
#     elif command_type == "Rearrange":
#         if checkItem_exists(items, item):
#             items.remove(item)
#             items.append(item)
#     command = input()
# print(", ".join(items))