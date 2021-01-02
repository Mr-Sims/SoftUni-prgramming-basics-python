flower_type = str(input())
flower_count = int(input())
budget = int(input())
price_per_flower = 0
if flower_type == "Roses":
    price_per_flower = 5
    if flower_count > 80:
        price_per_flower -= price_per_flower * 0.1
elif flower_type == "Dahlias":
    price_per_flower = 3.8
    if flower_count > 90:
        price_per_flower -= price_per_flower * 0.15
elif flower_type == "Tulips":
    price_per_flower = 2.8
    if flower_count > 80:
        price_per_flower -= price_per_flower * 0.15
elif flower_type == "Narcissus":
    price_per_flower = 3
    if flower_count < 120:
        price_per_flower += price_per_flower * 0.15
elif flower_type == "Gladiolus":
    price_per_flower = 2.5
    if flower_count < 80:
        price_per_flower += price_per_flower * 0.2
sum = flower_count * price_per_flower

if sum <= budget:
    left = budget - sum
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {left:.2f} leva left.")
elif sum > budget:
    need = sum - budget
    print(f"Not enough money, you need {need:.2f} leva more.")