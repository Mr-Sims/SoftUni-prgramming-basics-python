######################################################################################################33
##################################### Мое Решение  ##########################################################

# import re
# text = ""
# pattern = r"(^|(?<=\s))(%|\$)[A-Z]{1}[a-z]{2,}(\2)\:\s(?P<cell1>\[\d+\]\|)(?P<cell2>\[\d+\]\|)(?P<cell3>\[\d+\]\|)($|(?=\s))"
# valid = []
# line = input()
# while line:
#     text += line + " "
#     line = input()
#
# matches = re.finditer(pattern, text, re.IGNORECASE)
# for m in matches:
#     valid.append((m.group()).strip())
# [print(item)for item in valid]

######################################################################################################33
##################################### Решение Инес  ##########################################################

import re

data = input()
pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z\d-]+(\.[a-z]+)+($|(?=\s))"

while data:
    for el in re.finditer(pattern, data):
        print(el.group())
    data = input()