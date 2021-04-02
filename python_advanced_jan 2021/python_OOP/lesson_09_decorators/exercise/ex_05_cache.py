import functools


def cache(func):

    @functools.wraps(func)
    def wrapper(param):
        cache_key = param
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func(param)
        return wrapper.log[cache_key]
    wrapper.log = {}
    return wrapper


## Test case 1
@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


## Test case 2
fibonacci(3)
print(fibonacci.log)
