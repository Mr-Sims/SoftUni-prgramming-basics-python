num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def smallest(a, b, c):
    min_num = min(a, b, c)
    return min_num


print(smallest(num_1, num_2, num_3))