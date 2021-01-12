
from collections import deque
from datetime import datetime


def deque_queue_test():
    q = deque()
    for i in range(1 << 20):
        q.append(i)

    while q:
        x = q.popleft()


def list_queue_test():
    q = []
    for i in range(1 << 20):
        q.append(i)
    while q:
        x = q.pop(0)


def measure(action):
    start = datetime.now()
    action()
    end = datetime.now()
    print(f"Finished in {end - start}")


measure(deque_queue_test)
measure(list_queue_test)


