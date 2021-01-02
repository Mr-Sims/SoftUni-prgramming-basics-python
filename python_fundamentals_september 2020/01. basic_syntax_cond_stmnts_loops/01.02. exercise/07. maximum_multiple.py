# Given a Divisor and a Bound, find the largest integer N, such that:
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found

# МОЕ РЕШЕНИЕ
# max = 0
# divisor = int(input())
# bound = int(input())
#
# for i in range(1, bound+1):
#     if i <= bound and i % divisor == 0:
#         max = i
# print(max)

# МОЕ РЕШЕНИЕ 2
# divisor = int(input())
# bound = int(input())
# n = (bound // divisor) * divisor
# print(n)

######################################################
### НА СЛАВИ РЕШЕНИЕТО
# divisor = int(input())
# bound = int(input())
#
# for i in range(bound+1, 1, -1):
#     if i <= bound and i % divisor == 0:
#         print(i)
#         break



