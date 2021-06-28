PLAYER = 'A'
TARGET = 'x'


def read_board(n):
    matrix_list = []
    for row in range(n):
        row_data = input().split()
        matrix_list.append(row_data)
    return matrix_list


def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


mapper = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

matrix = read_board(5)


# matrix = [
#     ['x', 'x', '.', '.', 'x'],
#     ['x', '.', '.', '.', '.'],
#     ['.', '.', 'x', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['A', 'x', '.', '.', 'x'],
# ]

my_position = None
targets = []
shoot_targets = []

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        el = matrix[row_index][col_index]
        if el == PLAYER:
            my_position = (row_index, col_index)
        elif el == TARGET:

            targets.append((row_index, col_index))

n = int(input())

for _ in range(n):
    raw_command = input().split()
    command = raw_command[0]
    player_row, player_col = my_position
    if command == 'shoot':
        direction = raw_command[1]
        if direction == 'left':
            for col_index in range(player_col-1, -1, -1):
                element = matrix[player_row][col_index]
                if element == TARGET:
                    matrix[player_row][col_index] = '.'
                    shoot_targets.append([player_row, col_index])
                    break
        elif direction == 'right':
            for col_index in range(player_col+1, len(matrix)):
                element = matrix[player_row][col_index]
                if element == TARGET:
                    matrix[player_row][col_index] = '.'
                    shoot_targets.append([player_row, col_index])
                    break
        elif direction == 'up':
            for row_index in range(player_row-1, -1, -1):
                element = matrix[row_index][player_col]
                if element == TARGET:
                    matrix[row_index][player_col] = '.'

                    shoot_targets.append([row_index, player_col])
                    break
        elif direction == 'down':
            for row_index in range(player_row+1, len(matrix)):
                element = matrix[row_index][player_col]
                if element == TARGET:
                    matrix[row_index][player_col] = '.'

                    shoot_targets.append([row_index, player_col])
                    break
        # [print(row) for row in matrix]

    elif command == 'move':
        direction = raw_command[1]
        steps = int(raw_command[2])
        new_row = player_row + mapper[direction][0] * steps
        new_col = player_col + mapper[direction][1] * steps
        if is_in_range(new_row, new_col, len(matrix)):
            if matrix[new_row][new_col] == '.':
                my_position = (new_row, new_col)
                matrix[new_row][new_col] = 'A'
                matrix[player_row][player_col] = '.'
        # [print(row) for row in matrix]

if len(shoot_targets) == len(targets):
    print(f'Training completed! All {len(targets)} targets hit.')
else:
    targets_left = len(targets) - len(shoot_targets)
    print(f'Training not completed! {targets_left} targets left.')


[print(target) for target in shoot_targets]
