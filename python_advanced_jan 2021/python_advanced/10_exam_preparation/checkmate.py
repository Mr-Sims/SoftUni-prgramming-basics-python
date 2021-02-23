KING = "K"
QUEEN = "Q"


def read_board():
    board = [list(input().split()) for row in range(8)]
    return board


def find_king_position(board):
    for row_index in range(len(board)):
        if KING in board[row_index]:
            column_index = board[row_index].index(KING)
            return (row_index, column_index)


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    columns_count = len(board[0])
    (delta_row, delta_column) = deltas
    (row_index, column_index) = king

    while in_range(row_index, rows_count) and in_range(column_index, columns_count):
        if board[row_index][column_index] == QUEEN:
            return [row_index, column_index]

        row_index += delta_row
        column_index += delta_column


def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]

    queens = [
        search_with_deltas(board, king, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        print(*[row for row in queens], sep="\n")
    else:
        print("The king is safe!")

board = read_board()
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)



######################################################################################
###########
###  work in progress code:
#
#
# KING = "K"
# QUEEN = "Q"
#
#
# def read_board():
#     # return [
#     #     ['.', '.', '.', '.', '.', '.', '.', '.'],
#     #     ['Q', '.', '.', '.', '.', '.', '.', '.'],
#     #     ['.', 'K', '.', '.', '.', 'Q', '.', '.'],
#     #     ['.', '.', '.', 'Q', '.', '.', '.', '.'],
#     #     ['Q', '.', '.', '.', 'Q', '.', '.', '.'],
#     #     ['.', 'Q', '.', '.', '.', '.', '.', '.'],
#     #     ['.', '.', '.', '.', '.', '.', 'Q', '.'],
#     #     ['.', 'Q', '.', 'Q', '.', '.', '.', '.']
#     # ]
#
#     board = [list(input().split()) for row in range(8)]
#     return board
#
#
#
# def find_king_position(board):
#     for row_index in range(len(board)):
#         # for column_index in range(len(board[0])):                  # <- faster but not good looking
#         #     if board[row_index][column_index] == KING:
#         #         return (row_index, column_index)
#         if KING in board[row_index]:                                    # <- slower but better looking and understandable
#             column_index = board[row_index].index(KING)
#             return (row_index, column_index)
#
#
# # def get_capturing_queens(board, king):
# #     rows_count = len(board)
# #     columns_count = len(board[0])
# #     (king_row_index, king_column_index) = king
# #     queens = []
# #     # right
# #     for column_index in range(king_column_index + 1, columns_count):
# #         if board[king_row_index][column_index] == QUEEN:
# #             queens.append([king_row_index, column_index])
# #             break
# #
# #     # left
# #     for column_index in range(king_column_index-1, -1, -1):
# #         if board[king_row_index][column_index] == QUEEN:
# #             queens.append([king_row_index, column_index])
# #             break
# #
# def in_range(value, max_value):
#     return 0 <= value < max_value
#
#
# def search_with_deltas(board, king, deltas):
#     rows_count = len(board)
#     columns_count = len(board[0])
#     (delta_row, delta_column) = deltas
#     (row_index, column_index) = king
#
#     while in_range(row_index, rows_count) and in_range(column_index, columns_count):
#         if board[row_index][column_index] == QUEEN:
#             return [row_index, column_index]
#
#         row_index += delta_row
#         column_index += delta_column
#
#
# def get_capturing_queens(board, king):
#     deltas = [
#         (0, -1),
#         (-1, -1),
#         (-1, 0),
#         (-1, +1),
#         (0, +1),
#         (+1, +1),
#         (+1, 0),
#         (+1, -1)
#     ]
#
#     queens = [
#         search_with_deltas(board, king, delta)
#         for delta in deltas
#     ]
#     return [queen for queen in queens if queen]
#
#
# def print_result(queens):
#     print(*[row for row in queens], sep="\n")
#
#
# board = read_board()
# king = find_king_position(board)
# queens = get_capturing_queens(board, king)
# print_result(queens)