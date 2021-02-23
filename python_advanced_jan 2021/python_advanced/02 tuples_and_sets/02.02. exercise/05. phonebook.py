phonebook = {}

while True:
    command = input()
    if command.isdigit():
        n = int(command)
        break
    line = command.split("-")
    phonebook[line[0]] = line[1]

for i in range(n):
    query = input()
    if query in phonebook:
        print(f"{query} -> {phonebook[query]}")
    else:
        print(f"Contact {query} does not exist.")