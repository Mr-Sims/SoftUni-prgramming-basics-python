hall_price = int(input())

cake = hall_price * 0.2
drinks = (cake - (cake * 0.45))
animator = (hall_price * (1 / 3))

print(hall_price + cake + drinks + animator)