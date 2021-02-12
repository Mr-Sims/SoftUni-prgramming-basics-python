########################################################################################
### my solution

from collections import deque
number_of_pumps = int(input())
petrol_stations = deque()
for _ in range(number_of_pumps):
    petrol_stations.append([int(el) for el in input().split()])
tour = 0
gas_tank = 0
starting_station = 0
initial_stations = petrol_stations.copy()
while tour < number_of_pumps:
    current_station = petrol_stations[0]
    gas = current_station[0]
    distance = current_station[1]
    if gas + gas_tank >= distance:
        gas_tank += gas - distance
        tour += 1
        if starting_station == 0:
            starting_station = current_station
    else:
        tour = 0
        gas_tank = 0
        starting_station = 0

    petrol_stations.rotate(-1)
print(initial_stations.index(starting_station))


######################################################################################
###################### РЕШЕНИЕ ИНЕС  20/100 ##########################################

from collections import deque
petrol_pumps_count = int(input())
queue = deque()
truck_fuel = 0
for station in range(petrol_pumps_count):
    command = [int(el) for el in input().split()]
    queue.append(command)
for station in range(petrol_pumps_count):
    is_valid = True
    for circle_iteration in range(petrol_pumps_count):
        current_station = queue[station]
        petrol, distance_to_next = current_station
        truck_fuel += int(petrol)
        if truck_fuel >= int(distance_to_next):
            truck_fuel -= int(distance_to_next)
            queue.append(queue.popleft())
        else:
            is_valid = False
            break
        queue.append(current_station)
    if is_valid:
        print(station)
        break

######################################################################################
#####################################################################################
#################### МОЕ РЕШЕНИЕ - 20/100 ###########################################

from collections import deque
petrol_pumps_count = int(input())
truck_fuel = 0
queue = deque()
station_number = 0
for station in range(petrol_pumps_count):
    command = [int(el) for el in input().split()]
    queue.append(command)

while len(queue) > 0:
    current_station = queue.popleft()
    truck_fuel += int(current_station[0])
    if truck_fuel >= int(current_station[1]):
        truck_fuel -= int(current_station[1])

    else:
        queue.append(current_station)
        truck_fuel = 0
        station_number += 1
print(station_number)

######################################################################################
######################################################################################
#################### ЧУЖДО РЕШЕНИЕ - 100/100  #############################

# # # trucks
from collections import deque

n = int(input())
gas_stations = []
tank_capacity = 0
valid = True

for _ in range(n):
    gas_stations.append(input())  # 1st num is the amount of petrol # 2nd num is the distance to next station

que = deque(gas_stations)  # making possible to pop/append from BOTH sides of the list now.

for index in range(n):
    for el in que:
        petrol, distance = el.split()
        petrol = int(petrol)
        distance = int(distance)
        tank_capacity += petrol
        if tank_capacity >= distance:
            tank_capacity -= distance
        elif tank_capacity < distance:
            tank_capacity = 0
            que.rotate(-1)  # current station goes last, next station becomes 1st later
            valid = False
            break
    if valid:
        print(index)
        break
    else:
        valid = True

######################################################################################
######################################################################################
#################### ЧУЖДО РЕШЕНИЕ - 100/100  ################################


from collections import deque
n = int(input())
petrol = deque([])
dist = deque([])
tank = 0
current_index = 0
next_station = 0

for i in range(n):
    add_petrol, add_distance = input().split()
    petrol.append(add_petrol)
    dist.append(add_distance)

petrol.append(petrol[0])
dist.append(dist[0])

while True:
    add_to_tank = int(petrol[next_station]) - int(dist[next_station])
    if tank + add_to_tank < 0:
        current_index += 1
        next_station = 0
        tank = 0
        petrol.popleft()
        petrol.append(petrol[0])
        dist.popleft()
        dist.append(dist[0])
        continue
    else:
        tank += add_to_tank
        next_station += 1
        if next_station == n:
            break

print(current_index)
