n = int(input())
type_travel = input()
travel = 0
if n < 20 and type_travel == "day":
    travel = n * 0.79 + 0.7
elif n < 20 and type_travel == "night":
        travel = n * 0.9 + 0.7
elif 20 <= n < 100:
    travel = n * 0.09
elif n >= 100:
    travel = 0.06 * n
print(f"{travel:.2f}")










####################################

distance = int(input())
travel_time = input()

taxi_day = 0.7 + (distance * 0.79)
taxi_night = 0.7 + (distance * 0.9)
bus_price = distance * 0.09
train_price = distance * 0.06

if distance < 20:
    if travel_time == "day":
        print(f"{taxi_day:.2f}")
    elif travel_time == "night":
        print(f"{taxi_night:.2f}")
elif distance < 100:
    print(f"{bus_price:.2f}")
elif distance >= 100:
    print(f"{train_price:.2f}")