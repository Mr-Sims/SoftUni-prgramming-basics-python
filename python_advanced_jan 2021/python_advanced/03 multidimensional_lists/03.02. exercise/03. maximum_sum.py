####################################################################################################
####################################################################################################
####  v 1
import sys

rows, columns = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

current_sum = 0
maxed = -sys.maxsize
location = []
for row in range(rows-2):
    for col in range(columns-2):
        current_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if current_sum > maxed:
            maxed = current_sum
            location = [[matrix[row][col], matrix[row][col+1], matrix[row][col+2]],[matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]], [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]]

print(f"Sum = {maxed}")
for i in range(len(location)):
    print(" ".join(str(el) for el in location[i]))




#####################################################################################################
### v2
import sys

def read_matrix():
    (rows, columns) = [int(el) for el in input().split()]
    matrix = []
    for row in range(rows):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix

matrix = read_matrix()

rows = len(matrix)
columns = len(matrix[0])
current_sum = 0
maxed = -sys.maxsize
location = []
for row in range(rows-2):
    for col in range(columns-2):
        current_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if current_sum > maxed:
            maxed = current_sum
            location = [[matrix[row][col], matrix[row][col+1], matrix[row][col+2]],[matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]], [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]]

print(f"Sum = {maxed}")
for i in range(len(location)):
    print(" ".join(str(el) for el in location[i]))




####################################################################################################
########## with funcs

def read_matrix(is_test = False):
    if is_test:
        return [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4]
        ]
    else:
        rows, columns = [int(el) for el in input().split()]
        matrix = []
        for row in range(rows):
            row = [int(el) for el in input().split()]
            matrix.append(row)
        return matrix


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index+size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)
    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum< current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return(best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    best_sum_submatrix = []
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        best_sum_submatrix.append(row)
    print(f"Sum = {get_sum_of_submatrix(matrix, row_index, col_index, size)}")
    for i in best_sum_submatrix:
        print(" ".join([str(el) for el in i]))

matrix = read_matrix()
sub_matrix_size = 3
print_result(get_best_submatrix(matrix, sub_matrix_size), sub_matrix_size)

