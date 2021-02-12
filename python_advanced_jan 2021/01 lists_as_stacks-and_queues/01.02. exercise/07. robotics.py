from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots = []
available_robots = deque()

for el in data:
    robot_data = el.split("-")
    robot = {}
    robot["name"] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot["available_at"] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()
products = deque()

while not product == "End":
    products.append(product)
    product = input()

time = time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])
        robot = [el for el in robots if el == current_robot][0]
        robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])
            robot = [el for el in robots if el == current_robot][0]
            robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)

##########################################################
#############################
#############################
# else`s solution 07 ROBOTICS

#
# from collections import deque
# def add_second(hours, mins, secs):
#     secs += 1
#     if secs == 60:
#         secs = 0
#         mins += 1
#     if mins == 60:
#         mins = 0
#         hours += 1
#     if hours == 24:
#         hours = 0
#     return hours, mins, secs
#
#
# robots = input().split(";")
# available_robots = deque()
# working_robots = deque()
# robots_info_time = {}
# materials = deque()
# timer = []
# start = input().split(":")
# for x in start:
#     timer.append(int(x))
#
# for r in robots:
#     name, time = r.split("-")[0:]
#     time = int(time)
#     available_robots.append([name, time])
#     robots_info_time[name] = int(time)
#
# while True:
#     current_material = input()
#     if current_material == "End":
#         break
#     materials.append(current_material)
#
# while materials:
#     for rob_NA in working_robots:
#         rob_NA[1] -= 1
#         if rob_NA[1] == 0:
#             working_time_of_robot = robots_info_time[rob_NA[0]]
#             available_robots.append([rob_NA[0], working_time_of_robot])
#     working_robots = [r for r in working_robots if r[1] > 0]
#     timer = add_second(timer[0], timer[1], timer[2])
#     h, m, s = timer[0], timer[1], timer[2]
#
#     material = materials.popleft()
#     if not available_robots:
#         materials.append(material)
#         continue
#
#     if available_robots:
#         current_robot = available_robots.popleft()
#         working_robots.append(current_robot)
#         print(f"{current_robot[0]} - {material} [{h:02d}:{m:02d}:{s:02d}]")
#
# ###############################################################################
#
#
