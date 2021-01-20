def read_matrix(is_test = False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0]
        ]
    else:
        (rows, columns) = map(int, input().split(", "))
        matrix = []
        for row in range(rows):
            row = [int(el) for el in input().split(", ")]
            matrix.append(row)
        return matrix


matrix = read_matrix(is_test=False)

rows = len(matrix)
columns = len(matrix[0])
current_sum = 0
maxed = 0
location = [[],[]]
for row in range(rows-1):
    for col in range(columns-1):
        current_sum = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if current_sum > maxed:
            maxed = current_sum
            location = [[],[]]
            location[0].append(matrix[row][col])
            location[0].append(matrix[row][col+1])
            location[1].append(matrix[row+1][col])
            location[1].append(matrix[row+1][col+1])

for i in location:
    print(" ".join([str(el) for el in i]))
print(maxed)




#############################################################################################################################
#############################################################################################################################

### lecture solution


def read_matrix(is_test = False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0]
        ]
    else:
        (rows, columns) = map(int, input().split(", "))
        matrix = []
        for row in range(rows):
            row = [int(el) for el in input().split(", ")]
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
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(" ".join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, col_index, size))


matrix = read_matrix()
sub_matrix_size = 2
print_result(get_best_submatrix(matrix, sub_matrix_size), sub_matrix_size)

