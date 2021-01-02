import re
data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, data)
a = []
for match in matches:
    a.append(match.group())
print(*a)
