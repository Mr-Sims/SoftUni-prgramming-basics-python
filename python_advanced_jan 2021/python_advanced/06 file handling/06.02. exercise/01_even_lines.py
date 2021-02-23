import re


def write_result(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))


def replace_symbols(line):
    return re.sub("[-,\.\!\?]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_number in range(len(lines)):
        if row_number % 2 == 0:
            # formated_row = list(reversed([el for el in (replace_symbols(lines[row_number])).split()]))
            # print(" ".join(formated_row))
            replaced = replace_symbols(lines[row_number]).split()
            print(" ".join(replaced[::-1]))