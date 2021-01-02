stock = {}

while True:
    line = input()
    if line == "statistics":
        break

    key, value = line.split(": ")
    if key in stock:
        stock[key] += int(value)
    else:
        stock[key] = int(value)
#total_qnt = 0
print("Products in stock:")
for key, value in stock.items():
    print(f"- {key}: {value}")
    #total_qnt += value
print(f"Total Products: {len(stock)}")
#print(f"Total Quantity: {total_qnt}")
print(f"Total Quantity: {sum(stock.values())}")