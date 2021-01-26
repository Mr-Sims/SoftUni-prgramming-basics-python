###########################################################################################
###### simple dict, simple comprehensions

bunker = {category: [] for category in input().split(", ")}
n = int(input())
all_quantity = 0
all_quality = 0
for _ in range(n):
    category, item_name, item_params = input().split(" - ")
    item_quantity = int(item_params.split(";")[0].split(":")[1])
    item_quality = int(item_params.split(";")[1].split(":")[1])
    bunker[category].append(item_name)
    all_quantity += int(item_quantity)
    all_quality += int(item_quality)


print(f'Count of items: {all_quantity}')
aver_quality = all_quality / len(bunker)
print(f'Average quality: {aver_quality:.2f}')

print(*[f'{key} -> {", ".join(value)}' for key, value in bunker.items()], sep='\n')

##################################################################################################
#######################################
#### sofisticated dict, sofisticated print comprehension

bunker = {category: [] for category in input().split(", ")}
n = int(input())
bunker['all qnty'] = 0
bunker['all qlty'] = 0
for _ in range(n):
    category, item_name, item_params = input().split(" - ")
    item_quantity = int(item_params.split(";")[0].split(":")[1])
    item_quality = int(item_params.split(";")[1].split(":")[1])
    item_data = {item_name: {'quantity': item_quantity, 'quality': item_quality}}
    bunker[category].append(item_data)
    bunker['all qnty'] += int(item_quantity)
    bunker['all qlty'] += int(item_quality)


print(f'Count of items: {bunker["all qnty"]}')
print(f'Average quality: {bunker["all qlty"]/(len(bunker)-2):.2f}')
print(*[f'{category} -> {", ".join([list(d.keys())[0] for d in value])}' for category, value in bunker.items() if isinstance(bunker[category], list)], sep='\n')







