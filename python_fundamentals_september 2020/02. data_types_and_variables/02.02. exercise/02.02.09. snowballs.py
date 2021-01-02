number_snowballs = int(input())
max_value = 0
best_result = ""
for snowball in range(1, number_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max_value:
        max_value = snowball_value
        best_result = f"{snowball_snow} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"
print(best_result)
