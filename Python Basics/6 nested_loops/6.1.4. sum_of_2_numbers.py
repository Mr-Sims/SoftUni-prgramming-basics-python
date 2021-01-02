# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
# Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.



n1 = int(input())  #– начало на интервала – цяло число
n2 = int(input())  #– край на интервала – цяло число
magic_num = int(input())   #– магическото число – цяло число
count = 0
combo_found = False

for i in range(n1, n2 + 1):
    for j in range(n1, n2 + 1):
        count += 1
        if i + j == magic_num:
            print(f"Combination N:{count} ({i} + {j} = {magic_num})")
            combo_found = True
            break
    if combo_found:
        break
if not combo_found:
    print(f"{count} combinations - neither equals {magic_num}")




# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# •	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# •	Ако не е намерена комбинация отговаряща на условието
# o	"{броят на всички комбинации} combinations - neither equals {магическото число}"


# ЧУЖДО РЕШЕНИЕ

# x1 = int(input())
# x2 = int(input())
# y1 = 0
# y2 = 0
# n = int(input())
# combination = 0
# flag = False
# for i in range(x1, x2 + 1):
#     for j in range(x1, x2 + 1):
#         if i + j == n:
#             flag = True
#             combination = (x2 - x1 + 1) * (i - x1) + (j - x1 + 1)
#             y1 = i
#             y2 = j
#             break
#     if flag:
#         break
# if flag:
#     print(f'Combination N:{combination} ({y1} + {y2} = {(y1 + y2)})')
# else:
#     combination = (x2 - x1 + 1) ** 2
#     print(f'{combination} combinations - neither equals {n}')