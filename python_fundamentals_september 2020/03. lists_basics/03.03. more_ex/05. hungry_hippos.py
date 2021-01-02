matrix_rows = int(input())

matrix = []

for row in range(0, matrix_rows):
    matrix.append(list(map(int, input().split())))

for row in matrix:
    for col in row:
        if col
