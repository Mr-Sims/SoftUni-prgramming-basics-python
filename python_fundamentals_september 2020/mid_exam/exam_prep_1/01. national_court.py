worker_1 = int(input())
worker_2 = int(input())
worker_3 = int(input())
ppl_waiting = int(input())
ppl_per_hour = worker_1 + worker_2 + worker_3
hours = 0

while ppl_waiting > 0:
    hours += 1
    ppl_waiting -= ppl_per_hour
    if hours % 4 == 0:
        ppl_waiting += ppl_per_hour

print(f"Time needed: {hours}h.")