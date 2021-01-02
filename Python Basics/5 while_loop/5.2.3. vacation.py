money_needed = float(input())
money_have = float(input())
days = 0
spend = 0
while money_have < money_needed and spend < 5:
    action = input()
    amount = float(input())
    days += 1
    if action == "save":
        money_have += amount
        spend = 0
    elif action == "spend":
        money_have -= amount
        spend += 1
        if money_have < 0:
            money_have = 0
if spend == 5:
    print(f"You can't save the money.")
    print(days)
if money_have >= money_needed:
    print(f"You saved the money for {days} days.")






#
# money_needed = float(input())    #Пари, нужни за екскурзията - реално число;
# money_have = float(input())      #Налични пари - реално число.
# days_count = 0
#                         #След това многократно се четат по два реда:
# #action = input()                 #Вид действие – текст с две възможности: "spend" или "save";
# #amount = float(input())          #Сумата, която ще спести/похарчи - реално число.
# spend_count = 0
#
#
# while money_needed > money_have:
#     action = input()
#     amount = float(input())
#     days_count += 1
#     if action == "save":
#         money_have += amount
#     elif action == "spend":
#         spend_count += 1
#         if money_have >= amount:
#             money_have -= amount
#         elif amount >= money_have:
#             money_have = 0
#     if spend_count == 5:
#         break
#
# #    action = input()
# #    amount = float(input())
# if money_have >= money_needed:
#     print(f"You saved the money for {days_count} days.")
# else:
#     print(f"You can't save the money.\n{days_count}")


###
# money_needed = float(input())
# money_have = float(input())
# days_count = 0
# spend_count = 0
# while spend_count != 5 and money_needed > money_have:
#     action = input()
#     amount = float(input())
#     days_count += 1
#     if action == "save":
#         money_have += amount
#     elif action == "spend":
#         spend_count += 1
#         money_have -= amount
#         if money_have < amount:
#             money_have = 0
# if spend_count == 5:
#     print(f"You can't save the money.\n{days_count}")
# elif money_needed <= money_have:
#     print(f"You saved the money for {days_count} days.")