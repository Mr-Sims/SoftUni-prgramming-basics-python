# #############   75/100  ###############
#
# from collections import deque
# line = input()
# middle = int(len(line) / 2)
# heads = line[:middle]
# tail = deque()
#
# for i in range(len(heads)):
#     if heads[i] == "(":
#         tail.appendleft(")")
#     elif heads[i] == "{":
#         tail.appendleft("}")
#     elif heads[i] == "[":
#         tail.appendleft("]")
#
# tail = ''.join(tail)
# result = heads+tail
# if result == line:
#     print("YES")
# else:
#     print("NO")

############################## 100/100  #################################################

line = input()

is_balanced = True
stack = []

mirror = {"(": ")", "[": "]", "{": "}"}

for bracket in line:
    if len(line) % 2 != 0:
        is_balanced = False
        break
    if bracket in "({[":
        stack.append(bracket)
    else:
        current_bracket = stack.pop()
        if not mirror[current_bracket] == bracket:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")
