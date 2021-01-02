string = input()
new_string = ""
current_string = ""

index = 0

while index < len(string):

    if not string[index].isdigit():
        current_string += string[index]
        index += 1
    else:
        repeat = ""
        while index < len(string) and string[index].isdigit():
            repeat += string[index]
            index += 1

        repeat = int(repeat)
        current_string = current_string.upper() * repeat
        new_string += current_string
        current_string = ''


print(f'Unique symbols used: {len(set(new_string))}')
print(new_string)