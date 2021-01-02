# problem data
cake_price = 45
waffle_price = 5.8
crepe_price = 3.2

campaign_days = int(input()) #23
bakers = int(input()) #8
cakes = int(input()) #14
waffles = int(input()) #30
crepes = int(input()) #16
# problem logic
total_cakes = bakers * cakes * campaign_days * cake_price
total_waffles = bakers * waffles * campaign_days * waffle_price
total_crepes = bakers * crepes * campaign_days * crepe_price

total_products = (total_cakes + total_waffles + total_crepes) - ((total_cakes + total_waffles + total_crepes) * 1/8)

# print the output
print(total_products)