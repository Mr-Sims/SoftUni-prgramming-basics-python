from collections import deque

quantity_of_food = int(input())

queue = deque([int(el) for el in input().split()])
print(max(queue))

while queue:
    current_order = int(queue[0])
    if current_order <= quantity_of_food:
        quantity_of_food -= current_order
        queue.popleft()
    else:
        break
if queue:
    print("Orders left: ",end="")
    print(*queue)
else:
    print("Orders complete")



