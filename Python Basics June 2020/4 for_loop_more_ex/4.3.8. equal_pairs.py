# Дадени са 2*n-на брой числа.
# Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа.
# Напишете програма, която проверява дали всички двойки имат еднаква стойност
# или печата максималната разлика между две последователни двойки.
# Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value = {Value}" + стойността.
# В противен случай отпечатайте "No, maxdiff = {Difference}" + максималната разлика.

import sys
pairs_count = int(input())
max_sum = -sys.maxsize
min_sum = sys.maxsize
max_diff = -sys.maxsize
sum_nums = 0
sum_num1 = 0
for i in range(1, pairs_count + 1):
    num1 = int(input())
    num2 = int(input())
    sum_nums = num1 + num2
    if (num1 + num2) != sum_num1:
        max_diff = sum_nums - sum_num1
    if (num1 + num2) > max_sum:
        max_sum = (num1 + num2)
    if (num1 + num2) < min_sum:
        min_sum = (num1 + num2)
    sum_num1 = num1 + num2
if max_sum == min_sum:
    print(f"Yes, value={max_sum}")
else:
    print(f"No, maxdiff={abs(max_diff)}")
