######################################################################
############## creating a matrix with zeros ################################
# rows_count = 3
# columns_count = 2
# # v1
# matrix = []
# for row_index in range(rows_count):
#     row = []
#     for column_index in range(columns_count):
#         row.append(0)
#     matrix.append(row)
# print(matrix)
#v2
# matrix = [[0] * columns_count for _ in range(rows_count)]
# print(matrix)

####################################################################################################
#######################################creating a matrix with nums 1, 2, 3 #####################################################
# matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range(1, 4):
#        matrix[i].append(j)
# print(matrix)

################################################################
# ##################################################################
############## traversing through a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
