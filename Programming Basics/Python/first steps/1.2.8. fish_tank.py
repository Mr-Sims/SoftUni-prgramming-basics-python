# Problem data
lenght = int(input())
width = int(input())
height = int(input())
space_taken = float(input())

# Problem logic
aquarium_total = lenght * width * height
total_litres = aquarium_total * 0.001
percentage = space_taken * 0.01
water_needed = total_litres - (total_litres * percentage)
#Print the output
print(water_needed)