############### МОЕ РЕШЕНИЕ ##########################

# n = int(input())
# magic_nums = [5, 7, 11]
#
# for i in range(1, n + 1):
#     if sum(map(int, str(i))) in magic_nums:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")

################### МОЕ РЕШЕНИЕ 2 ################################

number = int(input())
magic = [5, 7, 11]
for i in range(1, number + 1):
    sum_of_digits = 0
    for digit in str(i):
        sum_of_digits += int(digit)
    if sum_of_digits in magic:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

############## РЕШЕНИЕ ОТ ЛАБ ДОКУМЕНТА #################

# n = int(input())
# magic_nums = [5, 7, 11]
#
# for num in range(1, n + 1):
#     sum_of_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#     if sum_of_digits in magic_nums:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")

###################################################


