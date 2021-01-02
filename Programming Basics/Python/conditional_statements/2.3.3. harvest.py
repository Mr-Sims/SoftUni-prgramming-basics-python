import math
area = int(input())
grapes_per_sq_m = float(input())
wine_need = int(input())
workers_count = int(input())
liter_wine = ((area * 0.4) * grapes_per_sq_m) / 2.5
diff = 0
if liter_wine < wine_need:
    diff = wine_need - liter_wine
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
elif liter_wine >= wine_need:
    diff = liter_wine - wine_need
    print(f"Good harvest this year! Total wine: {math.ceil(liter_wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.floor(diff / workers_count)} liters per person.")

###############################################################

# from math import floor
# from math import ceil
# vineyard_m2 = int(input())
# grape_per_m2 = float(input())
# wine_liters_needed = int(input())
# workers = int(input())
#
# total_harvest = vineyard_m2 * grape_per_m2
# harvest_for_wine = total_harvest * 0.4
# wine_liters_actual = harvest_for_wine / 2.5
#
# if wine_liters_actual < wine_liters_needed:
#     print(f"It will be a tough winter! More {floor(wine_liters_needed - wine_liters_actual)} liters wine needed.")
# elif wine_liters_actual >= wine_liters_needed:
#     print(f"Good harvest this year! Total wine: {floor(wine_liters_actual)} liters.")
#     print(f"{ceil(wine_liters_actual - wine_liters_needed)} liters left -> "
#           f"{ceil((wine_liters_actual - wine_liters_needed)/workers)} liters per person.")
