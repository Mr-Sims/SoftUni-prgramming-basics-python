# Напишете програма, която да пресмята резултата от игра. Първо получавате число, което показва колко хода ще продължи играта. После за всеки ход на играта ще получавате по едно ново число. Според интервала в който попада числото се прибавят точки. Ако числото е отрицателно или по-голямо 50, тогава то е невалидно. В началото на играта резултата е 0 и на всеки ход се прибавят точки по следният начин:
# •	От 0 до 9  20 % от числото
# •	От 10 до 19  30 % от числото
# •	От 20 до 29  40 % от числото
# •	От 30 до 39  50 точки
# •	От 40 до 50  100 точки
# •	Невалидно число  резултата се дели на 2
# Освен резултата програмата трябва да изкарва статистика за проценти числа в дадените интервали.

turns_count = int(input())
points = 0
cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
cat5 = 0
cat_invalid = 0
for turns in range(1, turns_count+1):
    num = int(input())
    if 0 <= num <= 9:
        points += (num * 20) /100
        cat1 += 1
    elif 10 <= num <= 19:
        points += (num * 30) / 100
        cat2 += 1
    elif 20 <= num <= 29:
        points += (num * 40) / 100
        cat3 += 1
    elif 30<= num <= 39:
        points += 50
        cat4 += 1
    elif 40 <= num <= 50:
        points += 100
        cat5 += 1
    elif num < 0 or num > 50:
        points = points/2
        cat_invalid += 1
print(f"{points:.2f}")
print(f"From 0 to 9: {((cat1/turns_count) * 100):.2f}%")
print(f"From 10 to 19: {((cat2/turns_count) * 100):.2f}%")
print(f"From 20 to 29: {((cat3/turns_count) * 100):.2f}%")
print(f"From 30 to 39: {((cat4/turns_count) * 100):.2f}%")
print(f"From 40 to 50: {((cat5/turns_count) * 100):.2f}%")
print(f"Invalid numbers: {((cat_invalid/turns_count) * 100):.2f}%")