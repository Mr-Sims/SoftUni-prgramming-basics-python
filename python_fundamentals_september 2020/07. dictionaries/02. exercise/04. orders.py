products_dict = {}

while True:

    line = input().split()
    if line[0] == 'buy':
        break

    product = line[0]
    price = float(line[1])
    amount = int(line[2])
    if product not in products_dict:
        products_dict[product] = [price, amount]
    else:
        products_dict[product][0] = price
        products_dict[product][1] += amount
for key, value in products_dict.items():
    end_price = products_dict[key][0] * products_dict[key][1]
    print(f"{key} -> {end_price:.2f}")

#########################################################################################
######################### Решение NESTED DICT ###################################################

# products = {}
#
# data = input()
#
# while not data == "buy":
#
#     product, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product not in products:
#         products[product] = {"price": price, "quantity": quantity}
#     else:
#         products[product]["price"] = price
#         products[product]["quantity"] += quantity
#     data = input()
#
# for product, price_qnt_data in products.items():
#     total_price = price_qnt_data["price"] * price_qnt_data["quantity"]
#     print(f"{product} -> {total_price:.2f}")











