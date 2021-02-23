rows, columns = [int(el) for el in input().split(", ")]

matrix = [0 for x in range(rows)]
for row in range(rows):
    lines = [int(x) for x in input().split(" ")]
    matrix[row] = lines

for c in range(columns):
    current_sum = 0
    for r in range(rows):
        current_sum += matrix[r][c]
    print(current_sum)

##################################################################
############### lab solution #####################################

sizes = list(map(int, input().split(", ")))
columns = sizes[1]
rows = sizes[0]
matrix = [[0] * columns for row in range(rows)]

for row in range(rows):
    lines = list(map(int, input().split()))
    for column in range(columns):
        matrix[row][column] = lines[column]
summed = [0] * columns

for column in range(columns):
    for row in range(rows):
        summed[column] += matrix[row][column]
    print(summed[column])

##########################################################################################
####################### funcs solution ####################################################


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
            row = [int(el) for el in input().split(" ")]
            matrix.append(row)
        return matrix


def column_sums(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    # sums = []
    # for col in range(columns):
    #     current_sum = 0
    #     for row in range(rows):
    #         current_sum += matrix[row][col]
    #     sums.append(current_sum)

    sums = [0] * columns
    for row in range(rows):
        for col in range(columns):
            sums[col] += matrix[row][col]
    return sums


def print_result(values):
    [print(x) for x in values]


matrix = read_matrix(is_test=True)
result = column_sums(matrix)
print_result(result)

############################################################
############# zip ##########################################

rows, columns = map(int, input().split(", "))
matrix = [[int(el) for el in input().split(" ")] for _ in range(rows)]

for col in zip(*matrix):
    print(sum(col))

