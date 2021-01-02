########################  ПЪРВО МОЕ РЕШЕНИЕ #########################################
items = input().split("|")
budget = float(input())
items_bought = []
for item in items:
    item_type, price = item.split("->")
    price = float(price)
    if (item_type == "Clothes" and price > 50.00) or (item_type == "Shoes" and price > 35.00) or (item_type == "Accessories" and price > 20.50):
        continue
    if budget >= price:
        budget -= price
        items_bought.append(price*1.4)
for el in items_bought:
    print(f"{el:.2f}",end=" ")
print()
profit = sum(items_bought) - (sum(items_bought) / 1.4)
print(f"Profit: {profit:.2f}")
end_budget = budget + sum(items_bought)
if end_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

################################### ВТОРО МОЕ РЕШЕНИЕ ####################################

items = input().split("|")
budget = float(input())
items_bought = []
profit = 0
for item in items:
    item_type, price = item.split("->")
    price = float(price)
    if (item_type == "Clothes" and price > 50.00) or (item_type == "Shoes" and price > 35.00) or (item_type == "Accessories" and price > 20.50):
        continue
    if budget >= price:
        budget -= price
        profit += price * 0.4
        items_bought.append(price*1.4)
budget += sum(items_bought)
for el in items_bought:
    print(f"{el:.2f}",end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")