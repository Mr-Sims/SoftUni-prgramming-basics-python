############## МОЕ РЕШЕНИЕ  ##########################

# n = int(input())
# even = []
# odd = []
# neg = []
# pos = []
#
# for el in range(0, n):
#     line = int(input())
#     if line % 2 == 0:
#         even.append(line)
#     else:
#         odd.append(line)
#     if line >= 0:
#         pos.append(line)
#     else:
#         neg.append(line)
# print_command = input()
# if print_command == "even":
#     print(even)
# elif print_command == "odd":
#     print(odd)
# elif print_command == "negative":
#     print(neg)
# elif print_command == "positive":
#     print(pos)

############### РЕШЕНИЕ ОТ LAB-A ##################################

n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_num = int(input())
    numbers.append(current_num)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in numbers:
        if not number % 2 == 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)
print(filtered)
