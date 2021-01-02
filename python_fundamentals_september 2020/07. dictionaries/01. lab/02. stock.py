line = input().split()
searched = [el for el in input().split()]
stock = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i+1])
    stock[key] = value

for element in searched:
    if element in stock:
        print(f"We have {stock[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")