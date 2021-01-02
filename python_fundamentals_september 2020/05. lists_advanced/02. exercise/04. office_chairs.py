number_of_rooms = int(input())
total_free_chairs = 0
game_on = True
for room in range(1, number_of_rooms+1):
    total_chairs, chairs_used = input().split()
    free_chairs = total_chairs.count("X") - int(chairs_used)
    if total_chairs.count("X") - int(chairs_used) < 0:
        print(f"{abs(free_chairs)} more chairs needed in room {room}")
        game_on = False
    total_free_chairs += free_chairs
if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")
