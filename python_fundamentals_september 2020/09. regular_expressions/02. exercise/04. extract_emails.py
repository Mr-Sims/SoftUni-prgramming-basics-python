import re
data = input()

pattern = r"((?<=^)|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z]+\-?[a-z]+(\.[a-z]+)+"

matches = re.finditer(pattern, data, re.IGNORECASE)
for el in matches:
    print(el.group())

