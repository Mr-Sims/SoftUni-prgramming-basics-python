######################################

def multiply(*args):
    prod = 1
    for el in args:
        prod *= el
    return prod

##################################
### reduce


from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x*y, args)

