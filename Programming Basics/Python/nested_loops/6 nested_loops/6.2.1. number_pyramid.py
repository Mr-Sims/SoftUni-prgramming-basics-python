n = int(input())
current = 1
current_is_bigger = False
for row in range(1,n + 1):
    for num in range(1, row + 1):
        if current > n:
            current_is_bigger = True
            break
        print(str(current) +" ", end = "")
        current += 1
    if current_is_bigger:
        break
    print()
##############################################

# n = int(input())
# number = 1
# flag = False
# for row in range(1, n + 1):
#     output = ''
#     for col in range(1, row + 1):
#         output += str(number) + ' '
#         if number == n:
#             flag = True
#             break
#         number += 1
#     print(output)
#     if flag:
#         break
