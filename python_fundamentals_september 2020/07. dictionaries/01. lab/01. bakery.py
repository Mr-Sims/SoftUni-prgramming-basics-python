line = input().split()

stock = {}

for el in range(0, len(line), 2):
    key = line[el]
    value = int(line[el+1])
    stock[key] = value

print(stock)
