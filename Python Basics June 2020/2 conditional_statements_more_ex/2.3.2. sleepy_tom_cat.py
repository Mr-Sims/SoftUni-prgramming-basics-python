tom_play_norm = 30000
workday_play = 63
holiday_play = 127
year = 365
holidays = int(input())
workdays = year - holidays
total_workday_play = workdays * workday_play
total_holiday_play = holidays * holiday_play

total_play_time = total_holiday_play + total_workday_play
if total_play_time <= tom_play_norm:
    time_left = tom_play_norm - total_play_time
    rest_hours = time_left // 60
    rest_minutes = time_left % 60
    print("Tom sleeps well")
    print(f"{rest_hours} hours and {rest_minutes} minutes less for play")
else:
    time_needed = total_play_time - tom_play_norm
    need_hours = time_needed // 60
    need_minutes = time_needed % 60
    print("Tom will run away")
    print(f"{need_hours} hours and {need_minutes} minutes more for play")