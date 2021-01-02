# Мими има закупени самолетни билети, но в последствие решава да си добави багаж към тях.
# Таксите за багаж се изчисляват въз основа на теглото на чекирания багаж:
# •	до 10кг – 20% от цената на багаж над 20кг
# •	между 10кг и 20кг вкл. – 50% от цената на багаж над 20кг.
# •	над 20кг – таксата се чете от конзолата

# В зависимост от броя на дните, които остават до пътуването, цената се оскъпява:
# •	повече от 30 дни - цената на багажа се оскъпява с 10%
# •	между 7 и 30 дни вкл. - цената на багажа се оскъпява с 15%
# •	по-малко от 7 дни - цената на багажа се оскъпява с 40%
# Напишете програма, която пресмята колко ще трябва да заплати Мими, спрямо горните условия.

price_luggage_over_20 = float(input())
luggage_weight = float(input())
days_until_trip = int(input())
luggage_count = int(input())
price_per_luggage = 0

if luggage_weight < 10:
    price_per_luggage = price_luggage_over_20 * 0.2
elif 10 <= luggage_weight <= 20:
    price_per_luggage = price_luggage_over_20 * 0.5
elif luggage_weight > 20:
    price_per_luggage = price_luggage_over_20

if days_until_trip > 30:
    price_per_luggage = price_per_luggage * 1.1
elif 7 <= days_until_trip <= 30:
    price_per_luggage = price_per_luggage * 1.15
elif days_until_trip < 7:
    price_per_luggage = price_per_luggage * 1.4
final_price = price_per_luggage * luggage_count
print(f"The total price of bags is: {final_price:.2f} lv.")







# Да се отпечата на конзолата сумата, която ще трябва да заплати Мими за багажите, в следния формат:
# •	" The total price of bags is: {цената на багажите} lv. "
# Сумата да бъде форматирана до втората цифра след десетичния знак.
