from collections import deque


def win_condition(palm, willow, crossette):
    if palm >= 3 and willow >= 3 and crossette >= 3:
        return True

firework_effects = deque([int(el) for el in input().split(', ') if int(el) > 0])
explosive_power = [int(el) for el in input().split(', ') if int(el) > 0]

is_perfect = False

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while firework_effects:

    current_effect = firework_effects.popleft()

    current_explosive_power = explosive_power.pop()
    possible_firework = current_effect + current_explosive_power

    if possible_firework % 3 == 0 and possible_firework % 5 == 0:
        crossette_fireworks += 1
    elif possible_firework % 3 == 0:
        palm_fireworks += 1
    elif possible_firework % 5 == 0:
        willow_fireworks += 1
    else:
        if current_effect - 1 <= 0:
            explosive_power.append(current_explosive_power)
        else:
            firework_effects.append(current_effect-1)
            explosive_power.append(current_explosive_power)
    if win_condition(palm_fireworks, willow_fireworks, crossette_fireworks) or not firework_effects or not explosive_power:
        break


if win_condition(palm_fireworks, willow_fireworks, crossette_fireworks):
    print("Congrats! You made the perfect firework show!")
    if firework_effects:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
    print(f"Palm Fireworks: {palm_fireworks}")
    print(f"Willow Fireworks: {willow_fireworks}")
    print(f"Crossette Fireworks: {crossette_fireworks}")


else:
    print("Sorry. You can’t make the perfect firework show.")
    if firework_effects:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
    print(f"Palm Fireworks: {palm_fireworks}")
    print(f"Willow Fireworks: {willow_fireworks}")
    print(f"Crossette Fireworks: {crossette_fireworks}")
