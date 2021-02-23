line = [int(el) for el in input().split(", ")]
rows = line[0]
columns = line[1]

matrix = []

for row in range(rows):
    matrix.append([])
    command = [int(el) for el in input().split(", ")]
    for column in range(columns):
        matrix[row].append(command[column])
sum_matrix = 0
for r in range(rows):
    for c in range(columns):
        sum_matrix += matrix[r][c]
print(sum_matrix)
#print(sum(sum(el) for el in matrix))
print(matrix)

#########################################################################
#########  lab solution  ################################################
rows, cols = [int(x) for x in input().split(", ")]

matrix = [0 for x in range(rows)]

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix[row] = lines
print(sum(sum(el) for el in matrix))
print(matrix)

#############################################################################
####### with funcs##############################################


def read_matrix():
    (rows, columns) = map(int, input().split(", "))
    matrix = []
    for row in range(rows):
        row = map(int, input().split(", "))
        matrix.append(list(row))
    return matrix


def sum_matrix():
    sum_matrix = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            sum_matrix += matrix[r][c]
    return sum_matrix


matrix = read_matrix()
suma = sum_matrix()

print(suma)
print(matrix)





