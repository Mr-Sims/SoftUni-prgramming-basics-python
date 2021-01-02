x = float(input())
y = float(input())
h = float(input())
door_area = 1.2 * 2
window_area = 1.5 * 1.5
house_front_wall = (x * x) - door_area
house_back_wall = x * x
house_walls = ((x * y) - window_area) * 2
total_house_walls_area = house_front_wall + house_back_wall + house_walls
house_walls_paint = total_house_walls_area / 3.4
print(f"{(house_walls_paint):.2f}")

house_roof_front = (x * h) / 2
house_roof_back = (x * h) / 2
house_roof_sides = (x * y) * 2
total_house_roof = house_roof_front + house_roof_back + house_roof_sides
house_roof_paint = total_house_roof / 4.3
print(f"{(house_roof_paint):.2f}")