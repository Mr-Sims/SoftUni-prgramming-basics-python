PLAYER = "P"
WALL = "X"


def create_field():
    size = int(input())
    board = [input().split() for el in range(size)]
    return board


def get_player_position(field):
    for row_index in range(len(field)):
        if PLAYER in field[row_index]:
            column_index = field[row_index].index(PLAYER)
            return (row_index, column_index)


def get_next_move(position, direction):
    dir_deltas = {
        'up': (-1, 0),
        'down': (+1, 0),
        'left': (0, -1),
        'right': (0, +1),
    }
    (row_index, column_index) = position
    (row_delta, column_delta) = dir_deltas[direction]
    return row_index + row_delta, column_index + column_delta


def out_of_bounds(row, col, field):
    if 0 <= row < len(field) and 0 <= col < len(field):
        return False
    return True


def wall_hit(row, col, field):
    if field[row][col] == WALL:
        return True
    return False


path = []
coins_collected = 0
field = create_field()
player_position = get_player_position(field)
is_lost = False
permited_commands = ["up", "down", "left", "right"]

while True:
    command = input()
    if not command:
        break
    if command in permited_commands:
        current_position = get_next_move(player_position, command)
        player_position = current_position

        if wall_hit(current_position[0], current_position[1], field) or out_of_bounds(current_position[0], current_position[1], field):
            is_lost = True
            break
        path.append(list(current_position))
        coins_collected += int(field[current_position[0]][current_position[1]])
        if coins_collected >= 100:
            break


if is_lost:
    print(f"Game over! You've collected {coins_collected //2 } coins.")
    print("Your path:")
    print(*path, sep="\n")
else:
    print(f"You won! You've collected {coins_collected} coins.")
    print("Your path:")
    print(*path,sep="\n")


