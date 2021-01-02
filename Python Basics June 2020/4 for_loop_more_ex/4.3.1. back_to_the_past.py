# Иванчо е на 18 години и получава наследство, което се състои от X сума пари и машина на времето.
# Той решава да се върне до 1800 година, но не знае дали парите ще са достатъчни, за да живее без да работи.
# Напишете програма, която пресмята, дали Иванчо ще има достатъчно пари, за да не се налага да работи до дадена година включително. Като приемем, че за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 лева.
# За всяка нечетна (1801,1803  и т.н.) ще харчи 12 000 + 50 * [годините, които е навършил през дадената година].
# Изход
# Да се отпечата на конзолата 1 ред. Сумата трябва да е форматирана до два знака след десетичната запетая:
# •	Ако парите са достатъчно:
# o	"Yes! He will live a carefree life and will have {N} dollars left." – където N са парите, които ще му останат.
# •	Ако парите НЕ са достатъчно:
# o	"He will need {М} dollars to survive." – където M е сумата, която НЕ достига.
# Вход
# Входът се чете от конзолата и съдържа точно 2 реда:
money_inherited = float(input())
last_year = int(input())
years = 18
for year in range(1800, last_year+1):
    if year % 2 == 0:
        money_inherited -= 12000
        years += 1
    else:
        money_inherited -= 12000 + 50 * years
        years += 1
if money_inherited >= 0:
    print(f"Yes! He will live a carefree life and will have {money_inherited:.2f} dollars left.")
else:
    print(f"He will need {abs(money_inherited):.2f} dollars to survive.")