budget = float(input())
extras_count = int(input())
costume_price = float(input())
decor = budget * 0.1
extras_costumes = extras_count * costume_price

if  extras_count > 150:
    extras_costumes *= 0.9
budget = (budget - decor) - extras_costumes
if budget >= 0:
    print("Action!")
    print(f"Wingard starts filming with {budget:.2f} leva left.")
elif budget < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget):.2f} leva more.")