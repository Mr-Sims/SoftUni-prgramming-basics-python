from collections import deque


def best_list_pureness(*values):
    queue = deque(values[0])
    K = values[1]
    biggest = 0
    best_pureness_cycle = 0
    for rotation in range(K + 1):
        pureness = 0
        for index, symbol in enumerate(queue):
            pureness += int(index) * int(symbol)
        if pureness > biggest:
            biggest = pureness
            best_pureness_cycle = rotation
        queue.rotate()
    result = f"Best pureness {biggest} after {best_pureness_cycle} rotations"
    return result


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)