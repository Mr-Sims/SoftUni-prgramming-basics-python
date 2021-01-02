# to_do_list = ["0" for _ in range(10)]
# command = input()
# while not command == "End":
#     data = command.split("-")
#     importance = int(data[0])
#     action = data[1]
#     to_do_list.remove("0")
#     to_do_list.insert(importance, action)
#     command = input()
# result = [el for el in to_do_list if el != "0"]
# print(result)

############################### РЕШЕНИЕ ЙОРДАН ДЖАМБАЗОВ от предишния fund ##########################################################

tasks = []

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0])
    task = tokens[1]
    tasks.append((priority, task))


tasks_in_priority = [task_name for priority, task_name in sorted(tasks)]
print(tasks_in_priority)