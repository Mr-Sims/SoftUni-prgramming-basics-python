####################################################################################################3
##################################### МОЕ РЕШЕНИЕ  #################################################################

# n = int(input())
# index = 0
# res = []
# while n > 0:
#     shell = 2 * (index+1)**2
#     if shell > n:
#         res.append(n)
#
#     else:
#         res.append(shell)
#     n -= shell
#     index += 1
# print(res)

####################################################################################################3
#####################################  РЕШЕНИЕ ИНЕС  #################################################################

# electrons = int(input())
#
# atom = []
# shell = 1
#
# while electrons > 0:
#     possible_electrons  = 2*shell**2
#     if possible_electrons > electrons:
#         atom.append(electrons)
#     else:
#         atom.append(possible_electrons)
#     electrons -= possible_electrons
#     shell += 1
#
# print(atom)

############################################################################
########################## РЕШЕНИЕ ЧАШО  ################################################

def el_dist(n):
    layer = 1
    res = []
    shell = 2*layer**2
    while n - shell > 0:
        res.append(shell)
        n -= shell
        layer += 1
        shell = 2*layer**2
    if n != 0:
        res.append(n)
    return res
print(el_dist(int(input())))