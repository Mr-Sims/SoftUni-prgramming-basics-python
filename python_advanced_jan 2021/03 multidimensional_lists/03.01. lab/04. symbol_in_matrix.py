def read_matrix(is_test = False):
    if is_test:
        return [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["X", "!", "@"]
        ]
    else:
        size = int(input())
        matrix = []
        for row in range(size):
            row = list(input())
            matrix.append(row)
        return matrix


def find_symbol(matrix):
    is_found = False
    symbol = input()
    size = len(matrix)
    col = 0
    row = 0
    for r in range(size):
        if is_found:
            break
        for c in range(size):
            if matrix[r][c] == symbol:
                row = r
                col = c
                is_found = True
                break
    if is_found:
        return f"({row}, {col})"
    else:
        return f"{symbol} does not occur in the matrix"


matrix = read_matrix()
print(find_symbol(matrix))

