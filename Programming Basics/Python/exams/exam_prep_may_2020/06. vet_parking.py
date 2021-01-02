# За всеки четен ден и нечетен час, паркингът таксува 2.50 лева.

# Във всеки нечетен ден и четен час таксата е 1.25 лева,

# във всички останали случаи се заплаща 1 лев.

# Таксуването става на всеки изминал час от деня.

# Всеки един от изходите трябва да бъде закръглен до втория знак след десетичната запетая.

# Изход:
# Да се отпечата на конзолата:
# •	За всеки изминал ден, общата сума, която трябва да се плати – "Day: {индексът на деня} –
# {общата сума за деня} leva"
# •	Когато програмата приключи - "Total: {общата сума за всички дни} leva"

days_count = int(input())
hours_count = int(input())
total = 0
for i in range(1, days_count+1):
    price_per_day = 0
    for j in range(1, hours_count+1):
        if i % 2 == 0 and j % 2 != 0:
            price_per_hour = 2.5
        elif i % 2 != 0 and j % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        price_per_day += price_per_hour * 1
    print(f"Day: {i} - {price_per_day:.2f} leva")
    total += price_per_day
print(f"Total: {total:.2f} leva")