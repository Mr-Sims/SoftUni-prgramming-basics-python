import functools


def type_check(t):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(param):
            if type(param) != t:
                return "Bad Type"
            return func(param)
        return wrapper
    return decorator


## Test case
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


# Test case 2
@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))