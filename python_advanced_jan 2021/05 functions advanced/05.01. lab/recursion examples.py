# ### recursion example
#
#
# def rec(n):
#     if n < 0:
#         print(f"end: {n}")
#         return 0 # base case
#     else:
#         print(f"forward pass {n}")
#         res = n + rec(n-1) # combinator
#         print(f"backward pass {n} {res}")
#         return res
#
#
# rec(5)
#
# ######################################################################################
# ######################################################################################
# ### recursion example v2
#
# def rec2(n, acc):
#     if n == 0:
#         print(f"end: {0}")
#         return acc # Base case
#     else:
#         print(f"forward pass {n}")
#         acc = acc + n # combinator
#         rec2(n-1, acc) # recursive call
#         print(f"backward pass {n} {acc}")
#
# rec2(5, 5)
#
# ###############################################################################################
# #################################################################################################
# #### Fibonacci recursion example
#
# def fib(n):
#     print(f"calculating fib{n}")
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# [print(fib(x)) for x in range(8)]

###############################################################################################
#################################################################################################
#### Thorsten`s Hanoi towers puzzle solver
#
#
# def move(from_tower, to_tower):
#     print("Move discs from {} to {}!".format(from_tower, to_tower))
#
#
# def hanoi(n, from_tower, helper_tower, to_tower):
#     if n== 0:
#         pass
#     else:
#         hanoi(n - 1, from_tower, to_tower, helper_tower)
#         move(from_tower, to_tower)
#         hanoi(n - 1, helper_tower, from_tower, to_tower)
#
#
# hanoi(3, "A", "B", "C")

# #######################################################################
# #######################################################################
# ### factoriel
#
# def fact(n):
#     if n == 0:
#         return 1
#
#     return n * fact(n-1)
#
#
# [print(fact(x)) for x in range(6)]
#######################################################################
#######################################################################
###






