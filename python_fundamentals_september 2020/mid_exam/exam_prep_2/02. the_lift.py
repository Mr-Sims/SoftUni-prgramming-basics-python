ppl_waiting = int(input())
current_state = [int(el) for el in input().split()]
MAX_LOAD = 4

for index in range(len(current_state)):
    while current_state[index] != MAX_LOAD:
        if ppl_waiting > 0:
            current_state[index] += 1
            ppl_waiting -= 1
        else:
            break

if ppl_waiting == 0 and 4 * len(current_state) > sum(current_state):
    print("The lift has empty spots!")
elif ppl_waiting > 0:
    print(f"There isn't enough space! {ppl_waiting} people in a queue!")

print(" ".join(str(el) for el in current_state))
