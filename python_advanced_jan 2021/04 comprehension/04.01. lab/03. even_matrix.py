def str_to_ints(strs):
    return [int(x) for x in strs]


def read_matrix():
    rows_count = int(input())
    return [str_to_ints(input().split(", ")) for _ in range(rows_count)]


def get_even(matrix):
    return [[x for x in row if x % 2 == 0] for row in matrix]


matrix = read_matrix()
result = get_even(matrix)
print(result)

########################################################################
########################################################################