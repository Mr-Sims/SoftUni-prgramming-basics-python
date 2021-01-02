string = input()
res = ","
for index in range(len(string)):
    if res[-1] == string[index]:
        continue
    else:
        res += string[index]
print(res[1::])

################### Чуждо ####################################
#
# line = input()
# new_str = ""
# new_letter = ""
# for letter in line:
#     if not letter == new_letter:
#         new_str += letter
#     new_letter = letter
# print(new_str)