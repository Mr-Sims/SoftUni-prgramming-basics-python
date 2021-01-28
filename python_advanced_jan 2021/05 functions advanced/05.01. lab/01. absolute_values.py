#############################################################
######### no func


print([abs(float(x)) for x in input().split()])

#########################################################
#### simple func

def absolute(num):
    return abs(num)


line = [absolute(float(x)) for x in input().split()]
print(line)

############################################################
############################################################
#### func with comprehension


def convert_iterable_to_absolute(nums_list):
    res = [abs(el) for el in nums_list]
    return res


line = [float(el) for el in input().split()]
print(convert_iterable_to_absolute(line))

##############################################################
###############################################################
### func with map and lambda


def convert_iterable_to_absolute(nums_list):
    res = list(map(lambda el: abs(el), nums_list))
    return res


line = map(lambda x: float(x), input().split())
print(convert_iterable_to_absolute(line))