###########################################################################################################
########################################################################################################
# Primary diagonal

n = int(input())

matrix = []

for row in range(n):
    matrix.append([])
    line = [int(el) for el in input().split(" ")]
    for column in range(n):
        matrix[row].append(line[column])

primary_diagonal_sum = 0

for r in range(n):
    primary_diagonal_sum += matrix[r][r]
print(primary_diagonal_sum)

#######################################################################################################
#######################################################################################################
############### primary diagonal with funcs ################################################################################
#

def read_matrix(is_test = False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]
    else:
        size = int(input())
        matrix = []
        for row in range(size):
            row = [int(el) for el in input().split(" ")]
            matrix.append(row)
        return matrix


def get_primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for r in range(len(matrix)):
        diagonal_sum += matrix[r][r]
    print(diagonal_sum)


matrix = read_matrix(is_test=True)
get_primary_diagonal_sum(matrix)


############################################################################################
#########################################################################################
## get sum below and above primary diagonal

def read_matrix(is_test = False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]
    else:
        size = int(input())
        matrix = []
        for row in range(size):
            row = [int(el) for el in input().split(" ")]
            matrix.append(row)
        return matrix


def get_sum_below_primary_diagonal_sum(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if c <= r:
                the_sum += matrix[r][c]
    print(the_sum)


def get_sum_above_primary_diagonal_sum(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(r, size):
            the_sum += matrix[r][c]
    print(the_sum)


def get_sum_below_primary_diagonal_sum_1(matrix): # without iterating through the whole matrix
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if r < c:
                break
            the_sum += matrix[r][c]
    print(the_sum)


matrix = read_matrix(is_test=True)
get_sum_below_primary_diagonal_sum(matrix)
get_sum_below_primary_diagonal_sum_1(matrix)
get_sum_above_primary_diagonal_sum(matrix)

#################################################################################################
#################################################################################################
## sum seconday diagonal

def read_matrix(is_test = False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]
    else:
        size = int(input())
        matrix = []
        for row in range(size):
            row = [int(el) for el in input().split(" ")]
            matrix.append(row)
        return matrix


def get_secondary_diagonal_sum(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for r in range(size):
        diagonal_sum += matrix[r][size - r - 1]
    print(diagonal_sum)


matrix = read_matrix(is_test=True)
get_secondary_diagonal_sum(matrix)

