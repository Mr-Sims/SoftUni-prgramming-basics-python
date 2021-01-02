################################   Решение ИНЕС   ##################################################


int_list = list(map(lambda x: int(x), input().split(", ")))
even_indices = [index for index in range(len(int_list)) if int_list[index] % 2 == 0]
print(even_indices)


##################################   Решение ИНЕС 2 #########################################################


# nums = list(map(int, input().split(", ")))
# even_nums = list(filter(lambda index: nums[index] % 2 == 0, range(len(nums))))
#
# print(even_nums)


#####################  РЕШЕНИЕ  НОВИ ЗНАНИЯ от lab-a   ############################


# int_list = list(map(lambda x: int(x), input().split(", ")))
# even_indices = [index for index in range(len(int_list)) if int_list[index] % 2 == 0]
#
# # for i in range(len(int_list)):
# #     if int_list[i] % 2 == 0:
# #         even_indices.append(i)
# print(even_indices)

#####################  РЕШЕНИЕ  НОВИ ЗНАНИЯ от lab-a   ############################

# for in enumerate в list comprehension

int_list = [int(el) for el in input().split(", ")]
even_indices = [index for index, num in enumerate(int_list) if num % 2 == 0]
print(even_indices)


######################### МОЕ РЕШЕНИЕ - СТАРИ ЗНАНИЯ РАБОТИ ###############################


# input_data = input().split(", ")
# int_list = [int(el) for el in input_data]
# even_indices = [for num in int_list]
#

# for index, symbol in enumerate(int_list):
#     if symbol % 2 == 0:
#         even_indices.append(index)
#
# print(even_indices)