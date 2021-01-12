line = input()
stack = []

for i in range(len(line)):
    char = line[i]
    if char == "(":
        stack.append(i)
    elif char == ")":
        j = stack.pop()
        print(line[j:i+1])

######################### Решение с enumerate #################################
line = input()
stack = []

for index, symbol in enumerate(line):
    if symbol == "(":
        stack.append(index)
    elif symbol == ")":
        open_bracket = stack.pop()
        print(line[open_bracket:index + 1])
