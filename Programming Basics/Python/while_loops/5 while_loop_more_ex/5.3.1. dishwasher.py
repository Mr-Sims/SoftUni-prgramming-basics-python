# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат за съдомиялна е достатъчно, за да измие определено количество съдове.
# Знае се, че всяка бутилка съдържа 750 мл. препарат,
# за 1 чиния са нужни 5 мл.,
# а за тенджера 15 мл.
# Приемете, че на всяко трето зареждане със съдове, съдомиялната се пълни само с тенджери,
# а останалите пъти с чинии.
# Докато не получите команда "End" ще продължите да получавате бройка съдове, които трябва да бъдат измити.

detergent = int(input()) * 750
line = input()
counter = 0
total_dishes = 0
total_pots = 0
detergent_used = 0
diff = 0
while line != "End":
    dishes_count = int(line)
    counter += 1
    if counter % 3 == 0:
        detergent_used += dishes_count * 15
        total_pots += dishes_count
    else:
        detergent_used += dishes_count * 5
        total_dishes += dishes_count
    diff = detergent - detergent_used
    if diff < 0 :
        break
    line = input()
if diff >= 0:
    print(f"Detergent was enough!\n{total_dishes} dishes and {total_pots} pots were washed.\nLeftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {abs(diff)} ml. more necessary!")



# Изход
# В случай, че количеството препарат е било достатъчно за измиването на съдовете:
# "Detergent was enough!"
# "{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
# "Leftover detergent {количество останал препарат} ml."
# В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
# "Not enough detergent, {количество не достигнал препарат} ml. more necessary!"
