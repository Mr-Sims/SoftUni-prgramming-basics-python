# Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.

months = int(input())
water_per_month = 20
net_per_month = 15
total_electricity = 0
total = 0
total_others = 0
for time in range(1, months+1):
    electricity_bill = float(input())
    others_per_month = (water_per_month + net_per_month + electricity_bill) + ((water_per_month + net_per_month + electricity_bill) * 0.2)
    total += electricity_bill + water_per_month + net_per_month + others_per_month
    total_electricity += electricity_bill
    total_others += others_per_month
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {(water_per_month * months):.2f} lv")
print(f"Internet: {(net_per_month * months):.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {(total / months):.2f} lv")
