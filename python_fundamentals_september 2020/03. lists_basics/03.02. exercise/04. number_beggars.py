#####################  МОЕ РЕШЕНИЕ  ####################################
numbers = input()
numbers_list = numbers.split(', ')
number_of_beggars = int(input())
beggars_list = [0] * number_of_beggars

while len(numbers_list) > 0:
    for index, beggar in enumerate(beggars_list):
        beggars_list[index] = int(numbers_list[0]) + int(beggar)
        numbers_list.pop(0)
        if len(numbers_list) == 0:
            break
print(beggars_list)


####################   ЧУЖДО РЕШЕНИЕ   ################################

# offers = input()
# beggars = int(input())
#
# offers_list = offers.split(", ")
# result = [0] * beggars
#
# for index in range(len(offers_list)):
#     offers_list[index] = int(offers_list[index])
#
# index = 0
#
# for element in offers_list:
#     result[index] += element
#     index += 1
#     if index == beggars:
#         index = 0
#
# print(result)

#########################################################















