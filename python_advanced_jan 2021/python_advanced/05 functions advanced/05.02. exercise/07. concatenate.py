def concatenate(*args):
    res = ""
    for i in args:
        res += i
    return res

print(concatenate("Soft", "Uni", "Is", "Great", "!"))

########################################################
# v2

def concatenate(*args):
    return ''.join(args)