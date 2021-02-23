from collections import deque

water = int(input())

thirsty_people = deque()

while True:
    command = input()
    if command == "Start":
        break
    thirsty_people.append(command)

while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break
    elif command.split(" ")[0] == "refill":
        water += int(command.split(" ")[1])
    else:
        person = thirsty_people.popleft()
        person_liters = int(command)

        if person_liters <= water:
            print(f"{person} got water")
            water -= person_liters
        else:

            print(f"{person} must wait")
