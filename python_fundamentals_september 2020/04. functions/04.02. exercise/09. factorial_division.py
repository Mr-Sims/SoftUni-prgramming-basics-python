# num = int(input())
# divisor = int(input())
#
#
# def factorial(a, b):
#     res1 = a
#     res2 = b
#     for i in range(a-1, 0, -1):
#
#         res1 *= i
#
#     for j in range(b-1, 0, -1):
#         res2 *= j
#
#     end_res = res1 / res2
#     return f"{end_res:.2f}"
#
#
# print(factorial(num, divisor))

######################### РЕШЕНИЕ 2 #####################################

num = int(input())
divisor = int(input())


def factorial(a):
    res = a
    for i in range(a-1, 0, -1):

        res *= i
    return res


result1 = factorial(num)
result2 = factorial(divisor)
print(f"{result1 / result2:.2f}")