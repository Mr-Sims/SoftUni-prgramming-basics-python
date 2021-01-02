budget = float(input())
line = input()
count = 0
total = 0
while line != "Stop":
    price = float(input())
    count += 1
    if count % 3 == 0:
        price *= 0.5
        budget -= price
        total += price
    else:
        budget -= price
        total += price
    if budget < 0:
        break
    line = input()

if budget >= 0:
    print(f"You bought {count} products for {total:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")