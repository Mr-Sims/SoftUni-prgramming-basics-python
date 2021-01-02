#Съществуват следните видове помещения със следните цени за престой:
# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще избере, той може да ползва различно намаление. Намаленията са както следва:
# След престоя оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) . Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея. Ако оценката му е негативна приспада от цената 10%.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - дни за престой - цяло число;
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment";
# •	Трети ред - оценка - "positive"  или "negative".
#На конзолата трябва да се отпечата един ред - цената за престоят му в хотела, форматирана до втория знак след десетичната запетая.
# room_for_1 = 18
# apartment = 25
# president_ap = 35

days = int(input())
room_type = str(input())
review = str(input())
nights = days - 1
price = 0
if room_type == "room for one person":
    if days < 10:
        if review == "positive":
            price = (nights * 18) * 1.25
        elif review == "negative":
            price = (nights * 18) * 0.9
    elif 10 <= days <= 15:
        if review == "positive":
            price = (nights * 18) * 1.25
        elif review == "negative":
            price = (nights * 18) * 0.9
    elif days > 15:
        if review == "positive":
            price = (nights * 18) * 1.25
        elif review == "negative":
            price = (nights * 18) * 0.9
if room_type == "apartment":
    if days < 10:
        if review == "positive":
            price = ((nights * 25) * 0.7) * 1.25
        elif review == "negative":
            price = ((nights * 25) * 0.7) * 0.9
    if 10 <= days <= 15:
        if review == "positive":
            price = ((nights * 25) * 0.65) * 1.25
        elif review == "negative":
            price = ((nights * 25) * 0.65) * 0.9
    if days > 15:
        if review == "positive":
            price = ((nights * 25) * 0.5) * 1.25
        elif review == "negative":
            price = ((nights * 25) * 0.5) * 0.9
if room_type == "president apartment":
    if days < 10:
        if review == "positive":
            price = ((nights * 35) * 0.9) * 1.25
        elif review == "negative":
            price = ((nights * 35) * 0.9) * 0.9
    if 10 <= days <= 15:
        if review == "positive":
            price = ((nights * 35) * 0.85) * 1.25
        elif review == "negative":
            price = ((nights * 35) * 0.85) * 0.9
    if days > 15:
        if review == "positive":
            price = ((nights * 35) * 0.8) * 1.25
        elif review == "negative":
            price = ((nights * 35) * 0.8) * 0.9
print(f"{price:.2f}")



# days = int(input())
# room = input()
# score = input()
#
# room_one = 18
# apartment = 25
# president = 35
# total = 0
# days_c = days - 1
#
#
#
# if days_c  < 10:
#     if room == "room for one person":
#         total = days_c * room_one
#     elif room == "apartment":
#         total = (days_c * apartment) * 0.70
#     else:
#         total = (days_c * president) * 0.90
# elif 10 <= days_c <= 15:
#     if room == "room for one person":
#         total = days_c * room_one
#     elif room == "apartment":
#         total = (days_c * apartment) * 0.65
#     else:
#         total = (days_c * president) * 0.85
# elif days_c > 15:
#     if room == "room for one person":
#         total = days_c * room_one
#     elif room == "apartment":
#         total = (days_c * apartment) * 0.50
#     else:
#         total = (days_c * president) * 0.80
#
#
# if score == "positive":
#     total = total + (total * 0.25)
# else:
#     total = total - (total * 0.10)
#
#
# print(f"{total:.2f}")