hour = int(input())
minutes = int(input())
extra_minutes = minutes +  15
if extra_minutes <= 59:
    print(f"{hour}:{extra_minutes}")
else:
    hour = hour + 1
    current_minutes = extra_minutes % 60
    if hour == 24:
        if current_minutes < 10:
            print(f"0:0{current_minutes}")
        elif current_minutes >= 10:
            print(f"0:{current_minutes}")
    if hour > 0 and hour <= 23:
        if current_minutes < 10:
            print(f"{hour}:0{current_minutes}")
        elif current_minutes >= 10:
            print(f"{hour}:{current_minutes}")