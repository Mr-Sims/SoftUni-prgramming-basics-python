def coordinates_valid(rows, cols, size):
    if (rows >= 0 and rows <= size-1) and (cols >= 0 and cols <= size-1):
        return True
    print("Invalid coordinates")


size = int(input())
matrix = [[int(x) for x in input().split()] for row in range(size)]
line = input()

while not line == "END":
    data = line.split()
    command = data[0]
    row_index = int(data[1])
    col_index = int(data[2])
    value = int(data[3])
    if command == "Add" and coordinates_valid(row_index, col_index, size):
        matrix[row_index][col_index] += value
    elif command == "Subtract" and coordinates_valid(row_index, col_index, size):
        matrix[row_index][col_index] -= value
    line = input()

for row in range(size):
    print(*[x for x in matrix[row]])

