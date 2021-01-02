budget = float(input())
flour_price = float(input())
pack_eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25

cozonac_price = 1 * pack_eggs_price + 1 * flour_price + (milk_price * 0.25)
total_number_cozonacs = 0
colored_eggs = 0
while True:
    budget -= cozonac_price
    if budget < 0:
        budget += cozonac_price
        break
    total_number_cozonacs += 1
    colored_eggs += 3
    if total_number_cozonacs % 3 == 0:
        colored_eggs -= total_number_cozonacs - 2

print(f"You made {total_number_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left")


# print(total_number_cozonacs)
# print(colored_eggs)
# print(budget)