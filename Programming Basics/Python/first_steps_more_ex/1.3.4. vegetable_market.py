price_veg = float(input())
price_fruit = float(input())
weight_veg = int(input())
weight_fruit = int(input())

zarzavat_total = (price_fruit * weight_fruit + price_veg * weight_veg) / 1.94

print(f"{(zarzavat_total):.2f}")