# Мое решение
age = int(input())
wash_machine = float(input())
toy_price = int(input())
toy_count = 0
brother = 0
total_gift_money = 0
for b_day in range(1, age+1):
    if b_day % 2 == 0:
        brother += 1
        total_gift_money += ((b_day * 10) / 2)
    else:
        toy_count += 1
total_toy_money = toy_count * toy_price
grand_total = total_gift_money + total_toy_money - brother
if grand_total >= wash_machine:
    print(f"Yes! {grand_total - wash_machine:.2f}")
else:
    print(f"No! {wash_machine - grand_total:.2f}")










# Чуждо решение
# age = int(input())
# washing_machine = float(input())
# toy_price = int(input())
# toy_count = 0
# savings = 0
# brother = 0
# for i in range(1, age + 1):
#     if i % 2 == 0:
#         savings += (10 + (toy_count - 1) * 10)
#         brother += 1
#     else:
#         toy_count += 1
# total_savings = (savings - brother) + (toy_count * toy_price)
#
# if total_savings >= washing_machine:
#     print(f"Yes! {(total_savings - washing_machine):.2f}")
# else:
#     print(f"No! {(washing_machine - total_savings):.2f}")
