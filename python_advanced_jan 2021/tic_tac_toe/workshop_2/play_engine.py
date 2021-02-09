from workshop_2_Ines import setup
from workshop_2_Ines.helpers import position_mapper


def is_position_valid(pos):
    if pos in range(1, 10):
        return True
    return False


def draw_board(board):
    print()
    for row in range(len(board)):
        print(f"| {' | '.join(board[row])} |")


def position_available(board, selected_position):
    row_num, col_num = position_mapper[selected_position]
    current_element = board[row_num][col_num]
    if not current_element == " ":
        return False
    return True


def play_turn(board, sign, selected_position):
    if position_available(board, selected_position):
        row_num, col_num = position_mapper[selected_position]
        board[row_num][col_num] = sign
        draw_board(board)
    else:
        current_selected_position = input(f"Select a valid available position[1-9]: ")
        current_selected_position = int(current_selected_position)
        play_turn(board, sign, current_selected_position)


def is_row_winner():
    for row_number in range(len(setup.board)):
        if setup.board[row_number].count("X") == 3 or setup.board[row_number].count("O") == 3:

            return True
    return False


def is_col_winner():
    first_col = setup.board[0][0] == setup.board[1][0] == setup.board[2][0] != " "
    second_col = setup.board[0][1] == setup.board[1][1] == setup.board[2][1] != " "
    third_col = setup.board[0][2] == setup.board[1][2] == setup.board[2][2] != " "
    if first_col or second_col or third_col:
        return True
    return False



def is_diagonal_winner():
    left_diagonal = setup.board[0][0] == setup.board[1][1] == setup.board[2][2] != " "
    right_diagonal = setup.board[0][2] == setup.board[1][1] == setup.board[2][0] != " "
    if left_diagonal or right_diagonal:
        return True
    return False


def has_won():
    if is_row_winner() or is_col_winner() or is_diagonal_winner():
        return True
    return False


def has_moves(counter):
    if counter < 10:
        return True
    return False


def play():
    turns_counter = 1
    while not has_won() and has_moves(turns_counter):

        current_selected_position = input(f"{setup.player_names[turns_counter%2]}, select a position[0-9]: ")
        while not current_selected_position.isdigit():
            current_selected_position = input(f"{setup.player_names[turns_counter % 2]}, select a position[0-9]: ")
        current_selected_position = int(current_selected_position)
        while not is_position_valid(current_selected_position):
            current_selected_position = input(f"{setup.player_names[turns_counter % 2]}, select a position[0-9]: ")
            current_selected_position = int(current_selected_position)
        play_turn(setup.board, setup.player_signs[turns_counter%2], current_selected_position)
        turns_counter += 1
    if has_won():
        print(f"{setup.player_names[(turns_counter-1)%2]} has won!")
    else:
        print("Draw!")