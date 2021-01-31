def recursive_power(num, power):

    if power == 1:
        return num

    num *= recursive_power(num, power - 1)
    return num


######################################################################################################
######################################################################################################


def recursive_power(num, power):

    if power == 0:
        return 1

    num *= recursive_power(num, power - 1)
    return num


###################################################################
####################################################################
#

def recursive_power(number, power):
    result = 0
    if power == 1:
        return
    recursive_power(number, power - 1)
    result += number ** power
    return result


print(recursive_power(2, 10))
print(recursive_power(10, 100))