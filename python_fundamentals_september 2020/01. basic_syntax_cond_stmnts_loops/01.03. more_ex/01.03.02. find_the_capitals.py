########## МОЕ РЕШЕНИЕ ###############

word = input()
capitals_list = list()

for index, symbol in enumerate(word):
    if chr(65) <= symbol <= chr(90):
        capitals_list.append(index)

print(capitals_list)

################# ЧУЖДО РЕШЕНИЕ - lazaroni от дискорда #########################

# n = list(input())
#
# result = []
# for i in range(len(n)):
#     if n[i].isupper():
#         result.insert(i, i)
#
# print(result)