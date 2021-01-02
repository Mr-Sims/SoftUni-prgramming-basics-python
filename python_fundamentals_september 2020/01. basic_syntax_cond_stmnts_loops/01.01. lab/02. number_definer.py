# n = float(input())
# if n < 0:
#     if 0 > n >= -1:
#         print("small negative")
#     elif n < -100000:
#         print("large negative")
#     else:
#         print("negative")
# elif n > 0:
#     if 0 < n < 1:
#         print("small positive")
#     elif n > 100000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     print("zero")
###########################
n = float(input())
if n == 0:
    print('zero')
else:
    if abs(n) < 1:
        print('small', end=' ')
    elif abs(n) > 1000000:
        print('large', end= ' ')
    if n > 0:
        print('positive')
    elif n < 0:
        print('negative')
