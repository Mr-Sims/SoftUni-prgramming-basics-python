#############################################################
######### no func


print([abs(float(x)) for x in input().split()])

#########################################################
#### simple func


def round_num(num):
    return round(num)


line = [round_num(float(x)) for x in input().split()]
print(line)

############################################################
############################################################
#### func with comprehension


def convert_iterable_to_rounded(nums_list):
    res = [round(el) for el in nums_list]
    return res


line = [float(el) for el in input().split()]
print(convert_iterable_to_rounded(line))





##############################################################
###############################################################
### func with map and lambda


def convert_iterable_to_rounded(nums_list):
    res = list(map(lambda el: round(el), nums_list))
    return res


line = map(lambda x: float(x), input().split())
print(convert_iterable_to_rounded(line))