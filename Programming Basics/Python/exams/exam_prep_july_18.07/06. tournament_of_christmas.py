# Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.
# Всеки ден получавате имена на игри до команда "Finish".
# Със спечелването на всяка една игра печелите по 20лв. за благотворителност.
# Трябва да изчислите колко пари сте спечелили на края на деня.
# Ако имате повече спечелени игри, отколкото загубени – вие сте победители този ден и увеличавате парите от него с 10%.
# При приключване на турнира ако през повечето дни сте били победители печелите турнира и увеличавате всичките спечелени пари с 20%.
# Никога няма да имате равен брой спечелени и загубени игри.

days_count = int(input())
money = 0
total_wins = 0
total_losses = 0
for i in range(1, days_count + 1):
    line = input()
    day_money = 0
    wins = 0
    losses = 0
    while line != "Finish":
        result = input()
        if result == "win":
            wins += 1
            day_money += 20
        elif result == "lose":
            losses += 1
        line = input()


        if line == "Finish":
            if wins > losses:
                day_money *= 1.1
                money += day_money
                day_money = 0
                total_wins += wins
                wins = 0
            elif losses > wins:
                money += day_money
                day_money = 0
                total_losses += losses
                losses = 0
if total_wins > total_losses:
    money *= 1.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")


# Изход
# Накрая се отпечатва един ред:
# •	Ако сте спечелили турнира:
#      	"You won the tournament! Total raised money: {спечелените пари}"
# •	Ако сте загубили на турнира:
# "You lost the tournament! Total raised money: {спечелените пари}"
# Резултатът да се форматира до втория знак след десетичната запетая.
