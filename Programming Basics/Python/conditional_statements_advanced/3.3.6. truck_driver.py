# Напишете програма която пресмята колко пари ще изкара шофьор на ТИР за един сезон.
# На входа програмата получава през кой сезон ще работи шофьора, както и колко километра на месец ще кара.
# Един сезон е 4 месеца. Според зависи сезона и броя километри на месец ще му се заплаща различна сума на километър:
# Изход
# На конзолата трябва да се отпечатат едно число:
# •	Заплатата на шофьора след данъците, форматирана до втория знак след десетичната запетая.

season = input()  # – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
km_per_month = float(input())  # –  Километри на месец – реално число
price_per_km = 0
tax = 0.9
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    elif season == "Winter":
        price_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    price_per_km = 1.45
salary = (price_per_km * km_per_month * 4) * tax
print(f"{salary:.2f}")