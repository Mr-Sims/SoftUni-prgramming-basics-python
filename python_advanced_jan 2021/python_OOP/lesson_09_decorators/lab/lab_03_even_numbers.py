import functools

def even_numbers(function):
    @functools.wraps(function)
    def wrapper(numbers):
        # result = [ch for ch in numbers if ch % 2 == 0]
        # return function(result)
        #
        result = function(numbers)
        return [x for x in result if x % 2 == 0]
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))