gifts_string = input()
gifts_list = gifts_string.split()

while True:
    line = input()
    if line == "No Money":
        break
    line_lst = line.split()

    if "OutOfStock" in line_lst:
        for command in line_lst:
            command_type, item = line.split()
        for index, element in enumerate(gifts_list):
            if element == item:
                gifts_list[index] = None
    elif "Required" in line_lst:
        for command in line_lst:
            command_type, item, i = line.split()
        for index, element in enumerate(gifts_list):
            if int(i) > len(gifts_list) - 1:
                gifts_list.append(item)
            else:
                gifts_list[int(i)] = item

    elif "JustInCase" in line_lst:
        for command in line_lst:
            command_type, item = line.split()
        gifts_list[-1] = item

for el in gifts_list:
    if not el == None:
        print(el, end=" ")

########################## ЧУЖДО РЕШЕНИЕ  #############################################

initial_input = input()
gifts = initial_input.split()

command = input()

while command != "No Money":
    if "OutOfStock" in command:
        gifts = ["None" if x == command.split()[1] else x for x in gifts]
    if "Required" in command and -1 < int(command.split()[2]) < len(gifts):
            gifts[int(command.split()[2])] = command.split()[1]
    if "JustInCase" in command:
        gifts[len(gifts)-1] = command.split()[1]
    command = input()

for gift in gifts:
    if gift !="None":
        print(gift, end=' ')
