# num = int(input())
# for i in range(1, num + 1):
#     for j in range(0, i):
#         print("*", end = "")
#     print()
# for i in range(num - 1, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()
    ##########################################
#
# desired_size = int(input())
# direction = 1
# current_size = 0
# while current_size < desired_size or (direction == -1 and current_size > 0):
#     current_size += direction
#     print('*' * current_size)
#     if desired_size == current_size:
#         direction = -1

################################################

# size = int(input())
# for i in range(1, size+1):
#     print(i * '*')
# for i in range(size-1, 0, -1):
#     print(i * '*')



#####################################
МОЕ РЕШЕНИЕ
n = int(input())
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print("*", end="")
    print()
for row in range(n-2, -1, -1):
    for col in range(row, -1, -1):
        print("*", end="")
    print()