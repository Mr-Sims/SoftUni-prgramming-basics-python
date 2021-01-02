#######################################   МОЕ РЕШЕНИЕ   ###########################################################

# employees_happiness_initial = [int(el) for el in input().split()]
# happiness_improve_factor = int(input())
#
# improved_happiness_list = [el * happiness_improve_factor for el in employees_happiness_initial]
# average_happiness = sum(improved_happiness_list) / len(improved_happiness_list)
# above_aver_happiness = [el for el in improved_happiness_list if el > average_happiness]
#
# if len(above_aver_happiness) >= len(improved_happiness_list) / 2:
#     print(f"Score: {len(above_aver_happiness)}/{len(improved_happiness_list)}. Employees are happy!")
# else:
#     print(f"Score: {len(above_aver_happiness)}/{len(improved_happiness_list)}. Employees are not happy!")

################################### РЕШЕНИЕ ОТ LAB-A  ###########################################################################

employees = input().split()
happi_factor = int(input())

employees = list(map(lambda x: int(x) * happi_factor, employees))

filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")

















