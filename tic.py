# ------- Global Variable --------- #




board = ['-','-','-',
        '-','-','-',
        '-','-','-'] 

game_still_going = True

winner = None

current_player = "X"

def display_board():
    for x in range(0,9,3):
        print(board[x], board[x+1],board[x+2],  sep = ' | ')


# Play game in tic tac toe

def play_game():
    display_board()
    
    while game_still_going:
        
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    #game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " won.")
    else:
        print('Tie.')

def handle_turn(player):

    print(player + "'s turn.")
    position = input('Choose a position from 1 - 9: ')

    valid = False
    while not valid:
        while position not in [str(i) for i in range(1,10)]:
            position = input('Invalid input! Choose a position from 1 - 9: ')

        position = int(position) -1

        if board[position] == '-':
            valid = True
        else:
            print("Invalid move!")
    
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner
    #check row
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner: 
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner : 
        winner = diagonal_winner
    return 

def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_still_going = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[6] == board[4] == board[2] != '-'

    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return

def check_if_tie():
    global game_still_going

    # Checking if the all board is fulled up
    if '-' not in board:
        game_still_going = False

def flip_player():

    global current_player


    #if the current player is X change flip in to O
    if current_player == 'X':
        current_player = 'O'
    else:
        # Vise versa to flip the player
        current_player = 'X'
    return 


play_game()
