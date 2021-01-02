n = int(input())
red = 0
orange = 0
yellow = 0
white = 0
black = 0
points = 0
others = 0
for i in range(1, n+1):
    color = input()
    if color == "red":
        red += 1
        points += 5
    elif color == "orange":
        orange += 1
        points += 10
    elif color == "yellow":
        yellow += 1
        points += 15
    elif color == "white":
        white += 1
        points += 20
    elif color == "black":
        black += 1
        points /= 2
    else:
        others += 1
print(f"Total points: {int(points)}")
print(f"Points from red balls: {red}")
print(f"Points from orange balls: {orange}")
print(f"Points from yellow balls: {yellow}")
print(f"Points from white balls: {white}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {black}")
