def read_matrix(is_test = False):
    if is_test:
        return [
            ["A", "B", "B", "D"],
            ["E", "B", "B", "B"],
            ["I", "J", "B", "B"]
        ]
    else:
        (rows, columns) = map(int, input().split(" "))
        matrix = []
        for row in range(rows):
            row = [el for el in input().split(" ")]
            matrix.append(row)
        return matrix


def find_equal_squares(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    equals_count = 0
    for row in range(rows - 1):
        for col in range(columns - 1):
            if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
                equals_count += 1
    return equals_count


matrix = read_matrix()
print(find_equal_squares(matrix))


#################################################################################################
################################################################################################
## else`s solution


# def read_matrix():
#     rows_count, columns_count = map(int, input().split(' '))
#     matrix = []
#     for row_index in range(rows_count):
#         row = [x for x in input().split()]
#         matrix.append(row)
#     return matrix
#
#
# def find_squares(matrix):
#     submatrix_size = 2
#     squares_count = 0
#     for row_index in range(len(matrix) - submatrix_size + 1):
#         for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
#             squares = set()
#             for r in range(row_index, row_index + submatrix_size):
#                 for c in range(col_index, col_index + submatrix_size):
#                     squares.add(matrix[r][c])
#             if len(squares) == 1:
#                 squares_count += 1
#     return squares_count
#
# matrix = read_matrix()
# print(find_squares(matrix))

