import re
furniture = []
total_spent = 0
pattern = r"^>>(?P<item>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>[0-9]+)"
while True:
    line = input()
    if line == "Purchase":
        break
    match = re.finditer(pattern, line)
    for m in match:
        i = m.group()
        item = m['item']
        price = m["price"]
        quantity = m['quantity']
        furniture.append(item)
        total_spent += float(price) * int(quantity)

print("Bought furniture:")
[print(item)for item in furniture]
print(f"Total money spend: {total_spent:.2f}")

#################################################################################################333
#################################################################################################333
############################### lazaroni  ##################################################################333

#
# import re
#
# total = 0
# items = []
#
# pattern = r'>>(?P<product>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<qty>\d+)(?!.)'
#
# furniture = input()
# while not furniture == 'Purchase':
#     if re.match(pattern, furniture):
#         data = re.search(pattern, furniture)
#         product, price, qty = data.group('product', 'price', 'qty')
#         items.append(product)
#         total += float(price) * int(qty)
#
#     furniture = input()
#
# print(f"Bought furniture:")
# [print(item)for item in items]
# print(f'Total money spend: {total:.2f}')