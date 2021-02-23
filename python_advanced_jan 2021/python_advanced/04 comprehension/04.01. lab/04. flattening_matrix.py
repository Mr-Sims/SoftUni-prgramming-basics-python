##################################################################
#############################

def read_matrix():
    rows = int(input())
    return [input().split(", ") for _ in range(rows)]

matrix = read_matrix()
print([int(x) for row in matrix for x in row])

##################################################################
#############################


def str_to_ints(strs):
    return [int(x) for x in strs]


def read_matrix():
    rows = int(input())
    return [str_to_ints(input().split(", ")) for _ in range(rows)]


matrix = read_matrix()
print([int(x) for row in matrix for x in row])


#############################################################################3
####################


def read_matrix():
    rows_count = int(input())
    return [input().split(", ") for _ in range(rows_count)]


def flatten(matrix):
    return [x for row in matrix for x in row]


def print_result(values):
    print([int(x) for x in values])


matrix = read_matrix()
result = flatten(matrix)
print_result(result)
