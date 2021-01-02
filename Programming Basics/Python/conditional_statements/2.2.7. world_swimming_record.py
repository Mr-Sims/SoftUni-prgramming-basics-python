import math
world_record = float(input())
distance = float(input())
time_seconds_for_1meter = float(input())

time_to_swim_distance = distance * time_seconds_for_1meter
resistance = math.floor(distance / 15) * 12.5
total_time = time_to_swim_distance + resistance

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {(total_time):.2f} seconds.")
else:
    seconds_needed = total_time - world_record
    print(f"No, he failed! He was {(seconds_needed):.2f} seconds slower.")
