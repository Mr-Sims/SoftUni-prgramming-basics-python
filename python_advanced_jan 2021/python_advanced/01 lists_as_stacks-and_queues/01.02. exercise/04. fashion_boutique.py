clothes = [int(el) for el in input().split(" ")]

capacity = int(input())
racks_needed = 1
rack = 0

while clothes:
    current_piece_of_clothing = clothes.pop()
    rack += current_piece_of_clothing
    if rack > capacity:
        clothes.append(current_piece_of_clothing)
    if rack >= capacity and len(clothes) > 0:
        rack = 0
        racks_needed += 1

print(racks_needed)