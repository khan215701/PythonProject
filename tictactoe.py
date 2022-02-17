board = []


def print_board():
    print('-----------')
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                print('| X ', end='')
            elif board[i][j] == 'O':
                print('| O ', end='')
            else:
                print('|  ', end='')
        print('|')
        print('----------')


def check_winner(player):
    check_symbol = 'X' if player else 'O'
    won = False
    for i in range(3):
        # check a horizontal way
        if board[i][0] == check_symbol and board[i][1] == check_symbol and board[i][2] == check_symbol:
            won = True
            break
        # check a vertical way
        if board[0][i] == check_symbol and board[1][i] == check_symbol and board[2][i] == check_symbol:
            won = True
            break
    # check a diagonal way
    if board[0][0] == check_symbol and board[1][1] == check_symbol and board[2][2] == check_symbol:
        won = True

    if board[2][0] == check_symbol and board[1][1] == check_symbol and board[0][2] == check_symbol:
        won = True

    return won


for i in range(3):
    row = []
    for j in range(3):
        row.append('')
    board.append(row)

# starting from here
game_continue = True
while game_continue:
    data = input('Enter your position e.g.(1,1) \n')

    try:
        position = data.split(',')
        x = int(position[0].strip())
        y = int(position[1].strip())
        skip_round = False
        if board[x-1][y-1] != '':
            print('sry, it position already taken try again')
            skip_round = True
        else:
            board[x-1][y-1] = 'X'
            print_board()

        if not skip_round:
            player_won = check_winner(True)
            if player_won:
                print('\U0001F389 \U0001F38A \U0001F388 \U0001F389 \U0001F38A \U0001F388')
                print('You won Congratulation')
                game_continue = False
    except:
        print("Invalid input, try again")