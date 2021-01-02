food_supply = int(input()) * 1000

line = input()

while line != "Adopted":
    food_ate = int(line)
    food_supply -= food_ate
    line = input()
if food_supply >= 0:
    print(f"Food is enough! Leftovers: {food_supply} grams.")
else:
    print(f"Food is not enough. You need {abs(food_supply)} grams more.")