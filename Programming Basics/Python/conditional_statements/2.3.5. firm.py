
from math import floor
hours_needed = int(input())
days = int(input())
overtimes_count = int(input())
work_days = days * 0.9
work_hours = work_days * 8
overtime_hours = overtimes_count * (2 * days)
total_hours = work_hours + overtime_hours
if floor(total_hours) >= hours_needed:
    print(f"Yes!{floor((total_hours - floor(hours_needed)))} hours left.")
elif floor(total_hours) < hours_needed:
    print(f"Not enough time!{hours_needed - floor(total_hours)} hours needed.")

