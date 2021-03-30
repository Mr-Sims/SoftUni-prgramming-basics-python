from math import sqrt


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True


def get_primes(iterable):
    for num in iterable:
        if is_prime(num) and num != 0 and num != 1:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))