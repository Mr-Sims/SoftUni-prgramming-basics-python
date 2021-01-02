# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта, който ще се практикува от учениците.
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището, форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“

season = input() #- “Winter”, “Spring” или “Summer”;
gender = input()# - “boys”, “girls” или “mixed”;
pupils_count = int(input())#Брой на учениците – цяло число
nights_count = int(input())# Брой на нощувките – цяло число
price_per_night = 0
sport = 0
discount = 1
final_price = 0
if season == "Winter":
    if gender == "boys":
        price_per_night = 9.6
        sport = "Judo"
    elif gender == "girls":
        price_per_night = 9.6
        sport = "Gymnastics"
    elif gender == "mixed":
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if gender == "boys":
        price_per_night = 7.2
        sport = "Tennis"
    elif gender == "girls":
        price_per_night = 7.2
        sport = "Athletics"
    elif gender == "mixed":
        price_per_night = 9.5
        sport = "Cycling"
elif season == "Summer":
    if gender == "boys":
        price_per_night = 15
        sport = "Football"
    elif gender == "girls":
        price_per_night = 15
        sport = "Volleyball"
    elif gender == "mixed":
        price_per_night = 20
        sport = "Swimming"
if 10 <= pupils_count < 20:
    discount = 0.95
elif 20 <= pupils_count < 50:
    discount = 0.85
elif pupils_count >= 50:
    discount = 0.5
final_price = (pupils_count * price_per_night * nights_count) * discount
print(f"{sport} {final_price:.2f} lv.")
