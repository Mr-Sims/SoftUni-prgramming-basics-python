# budget = int(input())
# season = str(input())
# fishermen_count = int(input())
# boat_cost = 0
# if season == "Spring":
#     boat_cost = 3000
#     if fishermen_count <= 6:
#         boat_cost *= 0.9
#     elif 7 <= fishermen_count <= 11:
#         boat_cost *= 0.85
#     elif fishermen_count > 12:
#         boat_cost *= 0.75
# elif season == "Summer" or season == "Autumn":
#     boat_cost = 4200
#     if fishermen_count <= 6:
#         boat_cost *= 0.9
#     elif 7 <= fishermen_count <= 11:
#         boat_cost *= 0.85
#     elif fishermen_count > 12:
#         boat_cost *= 0.75
# elif season == "Winter":
#     boat_cost = 2600
#     if fishermen_count <= 6:
#         boat_cost *= 0.9
#     elif 7 <= fishermen_count <= 11:
#         boat_cost *= 0.85
#     elif fishermen_count > 12:
#         boat_cost *= 0.75
#
# if fishermen_count % 2 == 0 and season != "Autumn":
#     boat_cost *= 0.95
#
# diff = boat_cost - budget
# if boat_cost < budget:
#     print(f"Yes! You have {abs(diff):.2f} leva left.")
# elif boat_cost > budget:
#     print(f"Not enough money! You need {diff:.2f} leva.")



budget = int(input())
season = str(input())
fishermen_count = int(input())
boat_cost = 0
if season == "Spring":
    boat_cost = 3000
elif season == "Summer" or season == "Autumn":
    boat_cost = 4200
elif season == "Winter":
    boat_cost = 2600
if fishermen_count % 2 == 0 and season != "Autumn":
    boat_cost -= boat_cost * 0.05
if fishermen_count <= 6:
    boat_cost -= boat_cost * 0.1
elif 7 <= fishermen_count <= 11:
    boat_cost -= boat_cost * 0.15
elif fishermen_count > 12:
    boat_cost -= boat_cost * 0.25
if boat_cost <= budget:
    print(f"Yes! You have {(budget - boat_cost):.2f} leva left.")
elif boat_cost > budget:
    print(f"Not enough money! You need {(boat_cost - budget):.2f} leva.")