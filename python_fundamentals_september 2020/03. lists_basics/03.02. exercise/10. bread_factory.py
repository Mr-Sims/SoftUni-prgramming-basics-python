initial_energy = 100
initial_coins = 100

work_day_events = input().split("|")
for event in work_day_events:
    action, number = event.split("-")
    if action == "rest":
        if initial_energy + int(number) > 100:
            print(f"You gained 0 energy.")
            print(f"Current energy: {initial_energy}.")
        else:
            initial_energy += int(number)
            print(f"You gained {int(number)} energy.")
            print(f"Current energy: {initial_energy}.")
    elif action == "order":
        if initial_energy - 30 < 0:
            initial_energy += 20
            print("You had to rest!")
        else:
            initial_energy -= 30
            print(f"You earned {int(number)} coins.")
            initial_coins += int(number)
    else:
        initial_coins -= int(number)
        if initial_coins > 0:
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            break

if initial_coins > 0:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

# rest-2|order-10|eggs-100|rest-10
# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000