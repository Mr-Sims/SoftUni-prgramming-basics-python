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
    return diagonal_sum


def get_secondary_diagonal_sum(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for r in range(size):
        diagonal_sum += matrix[r][size - r - 1]
    return diagonal_sum


matrix = read_matrix(is_test=False)
difference = abs(int(get_primary_diagonal_sum(matrix)) - int(get_secondary_diagonal_sum(matrix)))

print(difference)