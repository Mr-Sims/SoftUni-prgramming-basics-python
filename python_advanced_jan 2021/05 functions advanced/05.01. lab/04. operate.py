#########################################
### 4 operate with reduce and if/else

from functools import reduce


def operate(operator, *args):

    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)
    elif operator == "/":
        return reduce(lambda x, y: x / y, args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


#######################################
# 4 operate reduce with eval()

from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f'{x} {operator} {y}'), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

########################################
## 4 operate reduce with mapper

from functools import reduce
mapper = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}


def operate(operator, *args):
    return reduce(mapper[operator], args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))