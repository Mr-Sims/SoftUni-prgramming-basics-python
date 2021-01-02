#проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# Ако има такъв елемент, печата "Yes", "Sum = "  + неговата стойност;
# иначе печата "No", "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност).
import sys
n = int(input())
max_num = -sys.maxsize
sum_numbers = 0
for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num
if sum_numbers-max_num == max_num:
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(max_num-(sum_numbers-max_num))}")
