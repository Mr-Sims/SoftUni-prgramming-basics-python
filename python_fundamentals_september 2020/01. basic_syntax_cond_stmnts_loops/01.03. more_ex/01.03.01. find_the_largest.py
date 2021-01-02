########### МОЕ РЕШЕНИЕ ########################

n = input()
n_as_list = list(str(n))
max_number = ""

while len(n_as_list) > 0:
    max_number += max(n_as_list)
    n_as_list.remove(max(n_as_list))

print(max_number)

########  ЧУЖДО РЕШЕНИЕ - lazaroni от дискорда  ###############

# n = input()
#
# string_list = list(str(n))
# n_list = list(map(int, string_list))
#
# for i in range(len(n_list)):
#     print(max(n_list), end="")
#     n_list.remove(max(n_list))

######################################################