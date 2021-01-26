##############################################################
#######no compreh, only funcs


def create_matrix(rows, cols):
    matrix = []
    for row in range(rows_count):
        matrix.append([])
        for col in range(columns_count):
            matrix[row].append(f"{chr(97+row)}{chr(97+row+col)}{chr(97+row)}")
    return matrix


def print_matrix(matrix):
    for r in range(rows_count):
        print(" ".join(matrix[r]))


rows_count, columns_count = [int(el) for el in input().split(" ")]
matrix = create_matrix(rows_count, columns_count)
print_matrix(matrix)


################################################################
###############################################################
#### comprehension

rows_count, columns_count = [int(el) for el in input().split(" ")]

res = [[f"{chr(num)}{chr(nested_num)}{chr(num)}"for nested_num in range(num, num+columns_count)]for num in range(97, 97+rows_count)]

print(*[' '.join(iterable) for iterable in res], sep="\n")