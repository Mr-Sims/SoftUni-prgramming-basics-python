n = int(input())

guest_list = set()
arrived_list = set()
guest_list_counter = 0
while True:
    guest_list_counter += 1
    command = input()
    if command == "END":
        break
    if guest_list_counter <= n:
        guest_list.add(command)
    else:
        arrived_list.add(command)

did_not_come = list(guest_list - arrived_list)
print(len(did_not_come))
did_not_come.sort()
for _ in did_not_come:
    print(_)