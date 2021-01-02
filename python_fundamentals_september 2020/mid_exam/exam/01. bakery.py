
biscuits_per_worker = int(input())

workers_count = int(input())

competitor_biscuits_month = int(input())


produce_per_day = biscuits_per_worker * workers_count
total_produce = 0

for day in range(1, 30 + 1):
    if day % 3 == 0:
        total_produce += int(produce_per_day * 0.75)
    else:
        total_produce += produce_per_day


print(f"You have produced {int(total_produce)} biscuits for the past month.")
if total_produce > competitor_biscuits_month:
    perc = (total_produce-competitor_biscuits_month) / competitor_biscuits_month * 100
    print(f"You produce {perc:.2f} percent more biscuits.")
else:
    perc = (competitor_biscuits_month-total_produce)/ competitor_biscuits_month * 100
    print(f"You produce {perc:.2f} percent less biscuits.")