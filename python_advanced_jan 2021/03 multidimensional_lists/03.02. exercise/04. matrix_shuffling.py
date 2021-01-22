# ############################################################
# #### first try - 40/100
#
def create_matrix():
    rows, columns = [int(el) for el in input().split()]
    matrix = []
    for row in range(rows):
        row = [el for el in input().split()]
        matrix.append(row)
    return matrix


matrix = create_matrix()
while True:
    line = input()
    if line == "END":
        break
    data = line.split()

    try:
        command = data[0]
        row_1 = int(data[1])
        col_1 = int(data[2])
        row_2 = int(data[3])
        col_2 = int(data[4])
        if command == "swap":
            first_piece = matrix[row_1][col_1]
            second_piece = matrix[row_2][col_2]
            for row_index in range(len(matrix)):
                for col_index in range(len(matrix[0])):
                    current_item = matrix[row_index][col_index]
                    if current_item == first_piece:
                        matrix[row_index][col_index] = second_piece
                    if current_item == second_piece:
                        matrix[row_index][col_index] = first_piece
            for _ in matrix:
                print(" ".join(_))
    except:
        print("Invalid input!")

############################################################
#### second try - 100/100 with funcs


def create_matrix():
    rows, columns = [int(el) for el in input().split()]
    matrix = []
    for row in range(rows):
        row = [el for el in input().split()]
        matrix.append(row)
    return matrix


def swap_elements(matrix, row_1, col_1, row_2, col_2):
    first_piece = matrix[row_1][col_1]
    second_piece = matrix[row_2][col_2]
    matrix[row_1].pop(col_1)
    matrix[row_1].insert(col_1, second_piece)
    matrix[row_2].pop(col_2)
    matrix[row_2].insert(col_2, first_piece)
    return matrix


matrix = create_matrix()
while True:
    line = input()
    if line == "END":
        break
    data = line.split()
    command = data[0]
    if not command == "swap" or not len(data) == 5:
        print("Invalid input!")
    else:
        row_1, col_1, row_2, col_2 = [int(data[el]) for el in range(1, 5)]
        try:
            swap_elements(matrix, row_1, col_1, row_2, col_2)
            for _ in matrix:
                print(" ".join(_))
        except:
            print("Invalid input!")


#################################################################################################
#################################################################################################
##### Ines 80/100


rows, cols = [int(el) for el in input().split()]


def init_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        matrix.append([el for el in input().split()])
    return matrix


def check_if_index_is_valid(index_row, index_col, rows, cols):
    if 0 <= index_row < rows and 0 <= index_col < cols:
        return True
    return False


def check_if_command_is_valid(command, coords, rows, cols):
    if len(coords) == 4 and command == "swap":
        for index in range(0, len(coords), 2):
            if not check_if_index_is_valid(coords[index], coords[index+1], rows, cols):
                print("Invalid input!")
                return False
        return True
    print("Invalid input!")
    return False


def print_matrix(matrix):
    for row_index in range(0, len(matrix)):
        for col_index in range(0, len(matrix[row_index])):
            print(f"{matrix[row_index][col_index]} ", end="")
        print()


matrix = init_matrix(rows, cols)
data = input()
while not data == "END":
    splitted_data = data.split()
    try:
        command = splitted_data[0]
        coordinates = [int(el) for el in splitted_data[1:]]
    except:
        print("Invalid input!")
    if check_if_command_is_valid(command, coordinates, rows, cols):
        current_row = coordinates[0]
        current_col = coordinates[1]
        row_to_swap = coordinates[2]
        col_to_swap = coordinates[3]
        temp = matrix[current_row][current_col]
        matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
        matrix[row_to_swap][col_to_swap] = temp

        print_matrix(matrix)

    data = input()

