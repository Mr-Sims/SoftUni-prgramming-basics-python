number_of_commands = int(input())
database = {}
for com in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username in database:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            database[username] = plate
            print(f"{username} registered {plate} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username not in database:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            database.pop(username)
for key, value in database.items():
    print(f"{key} => {value}")
