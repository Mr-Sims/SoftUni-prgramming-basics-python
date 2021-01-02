pirate_ship = [int(el) for el in input().split(">")]
warship_ship = [int(el) for el in input().split(">")]

max_health = int(input())


while True:
    line = input()
    if line == "Retire":
        break
    command = line.split()[0]

    if command == "Fire":
        index = int(line.split()[1])
        damage = int(line.split()[2])
        if index in range(len(warship_ship)):
            warship_ship[index] -= damage
            if warship_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)

    elif command == "Defend":
        start_index = int(line.split()[1])
        end_index = int(line.split()[2])
        damage = int(line.split()[3])

        for sections in range(start_index, end_index+1):
            pirate_ship[sections] -= damage
            if pirate_ship[sections] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit(0)

    elif command == "Repair":
        index = int(line.split()[1])
        health = int(line.split()[2])
        if index in range(len(pirate_ship)):
            if pirate_ship[index] + health <= max_health:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = max_health

    elif command == "Status":
        counter = 0
        lowest = int(max_health * 0.2)
        for section in pirate_ship:
            if section < lowest:
                counter += 1
        print(f"{counter} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship_ship)}")

