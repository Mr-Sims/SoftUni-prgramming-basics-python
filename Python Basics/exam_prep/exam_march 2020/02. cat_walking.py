minutes_walk_day = int(input())
walks_per_day = int(input())
calories_per_day = int(input())
calories_burned_per_min = 5


calories_burned = (walks_per_day * minutes_walk_day) * calories_burned_per_min
need_to_burn = calories_per_day / 2
if calories_burned >= need_to_burn:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")