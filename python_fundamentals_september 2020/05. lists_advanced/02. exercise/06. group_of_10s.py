##########################################################################33
##################### МОЕ РЕШЕНИЕ - ТЪПО ###############################################
from math import ceil
initial_list = [int(el) for el in input().split(", ")]
n = ceil(max(initial_list) / 10)
master_list = [[] for _ in range(n)]
for age in initial_list:
    if 1 <= int(age) <= 10:
        master_list[0].append(age)
    elif 11 <= int(age) <= 20:
        master_list[1].append(age)
    elif 21 <= int(age) <= 30:
        master_list[2].append(age)
    elif 31 <= int(age) <= 40:
        master_list[3].append(age)
    elif 41 <= int(age) <= 50:
        master_list[4].append(age)
    elif 51 <= int(age) <= 60:
        master_list[5].append(age)
    elif 61 <= int(age) <= 70:
        master_list[6].append(age)
    elif 71 <= int(age) <= 80:
        master_list[7].append(age)
    elif 81 <= int(age) <= 90:
        master_list[8].append(age)
    elif 91 <= int(age) <= 100:
        master_list[9].append(age)
for index, symbol in enumerate(master_list):
    print(f"Group of {index+1}0's: {symbol}")

#########################################################################################
############################## Решение Таня Станева септември 2019 #######################################################


nums = [int(el) for el in input().split(", ")]

group = 10

while len(nums) > 0:
    filtered = [num for num in nums if num <= group]
    nums = [num for num in nums if num > group]

    print(f"Group of {group}'s: {filtered}")
    group += 10