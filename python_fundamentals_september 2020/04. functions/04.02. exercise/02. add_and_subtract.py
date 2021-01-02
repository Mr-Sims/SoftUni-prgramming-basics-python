num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    result = a + b
    return result


def subtract(z, x):
    result = z - x
    return result


print(subtract(sum_numbers(num_1, num_2), num_3))
