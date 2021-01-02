# Изход
# На конзолата трябва да се отпечата на един ред:
# •	Ако оставената храна Е достатъчна:
# o	"{килограма остатък} kilos of food left."
# 	Резултатът трябва да е закръглен към по-ниското цяло число
# •	Ако оставената храна НЕ Е достатъчна:
# o	“{килограма недостигат} more kilos of food are needed.”
# 	Резултатът трябва да е закръглен към по-високото цяло число
from math import ceil
from math import floor
days_count = int(input()) # брой дни – цяло число
food_left = int(input()) # оставена храна в килограми – цяло число
dog_food = float(input()) # храна на ден за кучето в килограми – реално число
cat_food = float(input())# храна на ден за котката в килограми– реално число
turtle_food = float(input())# храна на ден за костенурката в грамове – реално число
total_food = dog_food + cat_food + (turtle_food * 0.001)
food_need = total_food * days_count
if food_need < food_left:
    print(f"{floor(food_left - food_need)} kilos of food left.")
else:
    print(f"{ceil(food_need - food_left)} more kilos of food are needed.")