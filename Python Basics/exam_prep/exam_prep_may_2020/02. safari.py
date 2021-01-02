
# •	Цената на един литър гориво е 2.10 лв.
# •	Цената за екскурзовод е 100лв.
# •	В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%
# Вход
# От конзолата се четат 3 реда:
# •	Бюджет – реално число в интервала [0.00… 10000.00]
# •	Колко литра гориво ще са им нужни – реално число в интервала [1.00… 50.00]
# •	Ден от седмицата – текст с възможности "Saturday" и "Sunday"
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# "Safari time! Money left: {колко пари са им останали} lv. "
# •	Ако бюджетът не е достатъчен:
# "Not enough money! Money needed: {колко пари не им достигат} lv."
# Сумите трябва да са форматирани до втория знак след десетичната запетая.
budget = float(input())
fuel_needed = float(input())
day = input()
money_need = 0

fuel = 2.1
tour_guide = 100
if day == "Saturday":
    money_need = (fuel_needed * fuel + tour_guide) * 0.9
elif day == "Sunday":
    money_need = (fuel_needed * fuel + tour_guide) * 0.8
if money_need > budget:
    print(f"Not enough money! Money needed: {money_need-budget:.2f} lv.")
else:
    print(f"Safari time! Money left: {budget-money_need:.2f} lv.")








































# ЧУЖДО РЕШЕНИЕ

# budget = float(input())
#
# count_products = 0
# total = 0
# command = input()
# while command != "Stop":
#     product = command
#     price_product = float(input())
#     count_products += 1
#     if count_products % 3 == 0:
#         price_product *= 0.50
#     total += price_product
#
#     budget -= price_product
#     if budget < 0:
#         print("You don't have enough money!")
#         print(f"You need {abs(budget):.2f} leva!")
#         break
#
#     command = input()
# else:
#     print(f"You bought {count_products} products for {total:.2f} leva.")
