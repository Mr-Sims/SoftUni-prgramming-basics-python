# (^|(?<=\s))(%|\$)[A-Z]{1}[a-z]{2,}(\2):($|(?=\s))

import re
lines_number = int(input())
pattern = r"(^|(?<=\s))(%|\$)(?P<tag>[A-Z]{1}[a-z]{2,})(\2)\:\s(?P<cell1>\[\d+\]\|)(?P<cell2>\[\d+\]\|)(?P<cell3>\[\d+\]\|)($|(?=\s))"
for line_nr in range(lines_number):
    line = input()
    if re.match(pattern, line):
        matches = re.finditer(pattern, line)
        for match in matches:
            m = match.groupdict()
            tag = m["tag"]
            cell_1 = [el for el in m["cell1"] if el.isdigit()]
            cell_2 = [el for el in m["cell2"] if el.isdigit()]
            cell_3 = [el for el in m["cell3"] if el.isdigit()]
            let_1 = chr(int("".join(cell_1)))
            let_2 = chr(int("".join(cell_2)))
            let_3 = chr(int("".join(cell_3)))
            print(f"{tag}: {let_1}{let_2}{let_3}")
    else:
        print("Valid message not found!")
