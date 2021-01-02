HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)
fires = input().split("#")
water = int(input())
effort = 0
valid_cells_lst = []

for fire in fires:
    rng, intensity = fire.split(" = ")
    intensity = int(intensity)
    if (rng == "High" and intensity not in HIGH_RANGE) or (rng == "Medium" and intensity not in MEDIUM_RANGE) or (rng == "Low" and intensity not in LOW_RANGE):
        continue
    if water >= intensity:
        water -= intensity
        valid_cells_lst.append(intensity)
        effort += intensity * 0.25
print("Cells:")
for el in valid_cells_lst:
    print(f" - {el}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(valid_cells_lst)}")