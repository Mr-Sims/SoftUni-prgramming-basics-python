#####################################################################################################
############################ МОЕ РЕШЕНИЕ 50/100 ##################################################

# string = list(input())
# magnitude = 0
# new_string = string.copy()
# index = 0
#
# for el in range(len(string)-1):
#     counter = 0
#     if string[el] == ">":
#         magnitude += int(string[el+1])
#         if string[el+2] == ">" and magnitude > 1:
#             new_string.pop(el + 1 + index)
#             index -= 1
#             magnitude -= 1
#         else:
#             while magnitude > 0:
#                 new_string.pop(el + 1 + index)
#                 magnitude -= 1
#                 counter += 1
#             index -= counter
# print("".join(new_string))

#####################################################################################################
############################ ЧУЖДО РЕШЕНИЕ 100/100 ##################################################

#
# line = input().split(">")
# magnitude = 0
#
# new_string = []
#
# for el in line:
#     if el[0].isdigit():
#         magnitude += int(el[0])
#
#         if len(el) <= magnitude:
#             magnitude -= len(el)
#             el = ">"
#
#         else:
#             el = ">"+"".join(list(el[magnitude::]))
#             magnitude = 0
#     new_string.append(el)
# print("".join(new_string))

#####################################################################################################
############################ ЧУЖДО РЕШЕНИЕ 100/100 ##################################################


line = input()
res = ""
magnitude = 0

for char in range(len(line)):
    char_in_line = line[char]

    if char_in_line == ">":
        magnitude += int(line[char+1])
        res += char_in_line
    elif not magnitude == 0:
        magnitude -= 1
    else:
        res += char_in_line

print(res)