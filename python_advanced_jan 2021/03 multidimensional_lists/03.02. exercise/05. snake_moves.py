###########################################################
### v1 - funcs, using deque + rotate

from collections import deque

rows, columns = [int(el) for el in input().split()]
snake = deque(list(input()))


def create_matrix(rows, columns, snake):
    matrix = []
    for row in range(rows):
        matrix.append([])
        for col in range(columns):
            matrix[row].append(snake[0])
            snake.rotate(-1)
    return matrix


def print_matrix(matrix):
    for i in range(rows):
        if i % 2 != 0:
            matrix[i].reverse()
        print("".join(matrix[i]))



matrix = create_matrix(rows, columns, snake)
print_matrix(matrix)


###########################################################
###########################################################
### v2 - no funcs, using only lists and list slicing

# rows, cols = [int(el) for el in input().split()]
# word = input()
# count = 0
# a_list = []
#
# for _ in range(rows * cols):
#     if count == len(word):
#         count = 0
#     a_list.append(word[count])
#     count += 1
#
# a_list = ''.join(a_list)
# start, stop = 0, cols
#
# for i in range(rows):
#     if i % 2 != 0:
#         print(a_list[stop - 1:start - 1:-1])
#     else:
#         print(a_list[start:stop])
#     start += cols
#     stop += cols

###########################################################
###########################################################
### v3
