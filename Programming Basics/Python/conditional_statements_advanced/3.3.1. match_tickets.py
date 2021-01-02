# VIP – 499.99
# Normal – 249.99
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспорт:
# Напишете програма, която да пресмята дали с останалите пари от бюджета могат да си купят билети за избраната категория. И колко пари ще им останат или ще са им нужни.
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

budget = float(input())
category_ticket = input()
ppl_count = int(input())
money_left = 0
ticket_price = 0
if 1 <= ppl_count <= 4:
    money_left = budget * 0.25
elif 5 <= ppl_count <= 9:
    money_left = budget * 0.40
elif 10 <= ppl_count <= 24:
    money_left = budget * 0.5
elif 25 <= ppl_count <= 49:
    money_left = budget * 0.6
elif ppl_count >= 50:
    money_left = budget * 0.75
if category_ticket == "VIP":
    ticket_price = ppl_count * 499.99
    if ticket_price <= money_left:
        print(f"Yes! You have {(money_left - ticket_price):.2f} leva left.")
    else:
        print(f"Not enough money! You need {(ticket_price - money_left):.2f} leva.")
elif category_ticket == "Normal":
    ticket_price = ppl_count * 249.99
    if ticket_price <= money_left:
        print(f"Yes! You have {(money_left - ticket_price):.2f} leva left.")
    else:
        print(f"Not enough money! You need {(ticket_price - money_left):.2f} leva.")
