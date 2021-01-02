ornament_set_price = 2
tree_skirt_price = 5
garlands_price = 3
lights_price = 15
quantity = int(input())
days = int(input())
spirit = 0
cost = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 10 == 0:
        spirit -= 20
        cost += tree_skirt_price + garlands_price+ lights_price
        if i % 10 == 0 and i == days:
            spirit -= 30
    if i % 5 == 0:
        cost += quantity * lights_price
        spirit += 17
        if i % 5 == 0 and i % 3 == 0:
            spirit += 30
    if i % 3 == 0:
        cost += quantity * tree_skirt_price + quantity * garlands_price
        spirit += 13
    if i % 2 == 0:
        cost += quantity * ornament_set_price
        spirit += 5
print(f"Total cost: {cost}\nTotal spirit: {spirit}")