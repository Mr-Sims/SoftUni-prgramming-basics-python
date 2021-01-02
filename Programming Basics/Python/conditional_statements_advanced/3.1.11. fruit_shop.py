fruit = input()
day = input()
quantity = float(input())
price = 0
is_invalid = False
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = quantity * 2.5
    elif fruit == "apple":
        price = quantity *  1.2
    elif fruit == "orange":
        price = quantity *  0.85
    elif fruit == "grapefruit":
        price = quantity *  1.45
    elif fruit == "kiwi":
        price = quantity *  2.70
    elif fruit == "pineapple":
        price = quantity *  5.5
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        is_invalid = True
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = quantity * 2.7
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.9
    elif fruit == "grapefruit":
        price = quantity * 1.6
    elif fruit == "kiwi":
        price = quantity * 3
    elif fruit == "pineapple":
        price = quantity * 5.6
    elif fruit == "grapes":
        price = quantity * 4.2
    else:
        is_invalid = True
else:
    is_invalid = True

if (is_invalid):
    print("error")
else:
    print(f"{price:.2f}")




# fruit = input()
# day_of_the_week = input()
# quantity = float(input())
# price = 0
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
# if day_of_the_week not in days or fruit not in fruits:
#     print(f'error')
#     quit()
# if fruit == 'banana':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 2.70
#     else:
#         price = 2.50
# elif fruit == 'apple':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 1.25
#     else:
#         price = 1.20
# elif fruit == 'orange':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 0.90
#     else:
#         price = 0.85
# elif fruit == 'grapefruit':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 1.60
#     else:
#         price = 1.45
# elif fruit == 'kiwi':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 3
#     else:
#         price = 2.70
# elif fruit == 'pineapple':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 5.60
#     else:
#         price = 5.50
# elif fruit == 'grapes':
#     if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#         price = 4.20
#     else:
#         price = 3.85
# total = price * quantity
# print(f'{total:.2f}')


