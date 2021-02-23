#######################################################################################################
######################################################################################################
### working code 100/100

n = int(input())


def matrix_create(size, is_test=False):
    matrix = []
    for r in range(n):
        line = list(input())
        matrix.append(line)
    return matrix


def is_valid_pos(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row+rows[index]
        potential_col = col+cols[index]
        if is_valid_pos(potential_row, potential_col):
            potential_pos = matrix[potential_row][potential_col]
            if potential_pos == "K":
               kills += 1
    return kills


removed_counter = 0
matrix = matrix_create(n)

while True:
    max_kills = 0
    killer_pos = []
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == "K":
                kills = calculate_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_pos = [row_index, col_index]
    if killer_pos:
        matrix[killer_pos[0]][killer_pos[1]] = '0'
        removed_counter += 1
    else:
        break
print(removed_counter)



######################################################################################################
######################################################################################################
#### initial code

size = int(input())


def matrix_create(size, is_test=False):
    matrix = []
    if is_test:
        matrix = [
            ['0','K','0','K','0'],
            ['K','0','0','0','K'],
            ['0','0','K','0','0'],
            ['K','0','0','0','K'],
            ['0','K','0','K','0']
        ]
    else:
        for r in range(size):
            line = list(input())
            matrix.append(line)
    return matrix


def check_if_index_is_valid(row, col, size, matrix):
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "K":
            return True
    return False


matrix = matrix_create(size, is_test=False)
hits = 0

for row_index in range(size):
    for column_index in range(size):
        if matrix[row_index][column_index] == "K":
            if check_if_index_is_valid(row_index-2, column_index-1, size, matrix): # 1. check [r-2][c-1]
                hits += 1
            if check_if_index_is_valid(row_index-2, column_index+1, size, matrix): # 2. check [r-2][c+1]
                hits += 1
            if check_if_index_is_valid(row_index-1, column_index-2, size, matrix): # 3. check [r-1][c-2]
                hits += 1
            if check_if_index_is_valid(row_index-1, column_index+2, size, matrix): # 4. check [r-1][c+2]
                hits += 1
            if check_if_index_is_valid(row_index+1, column_index-2, size, matrix): # 5. check [r+1][c-2]
                hits += 1
            if check_if_index_is_valid(row_index+1, column_index+2, size, matrix): # 6. check [r+1][c+2]
                hits += 1
            if check_if_index_is_valid(row_index+2, column_index-1, size, matrix): # 7. check [r+2][c-1]
                hits += 1
            if check_if_index_is_valid(row_index+2, column_index+1, size, matrix): # 8. check [r+2][c+1]
                hits += 1
            else:
                continue
        else:
            continue
print(hits)
