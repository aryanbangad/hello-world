print('Welcome to Tic Tac Toe!')

player1 = input("what is your name player 1?: ")
player2 = input("what is your name player 2?: ")
def example_board():
	print('   |   | ')
	print(' 7 | 8 | 9')
	print('   |   | ')
	print('------------')
	print('   |   | ')
	print(' 4 | 5 | 6')
	print('   |   | ')
	print('-----------')
	print('   |   | ')
	print(' 1 | 2 | 3')
	print('   |   | ')
	print('enter positoin by reffering to the example board')
	
	
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_input():
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(player1+ ' Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
import random
def choose_first():
    if random.randint(0 , 1) == 0:
        return player2
    else:
        return player1
def space_check(board, position):
    
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board,name):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = input('Choose your next position '+ name +' (1-9) ')
    return int(position)
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
	


while True:
    
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == player1:
            # Player1's turn.
            print('this is a example board:')
            example_board()
			
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! '+player1+  ' has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player2

        else:
            # Player2's turn.
            print('this is a example board:')
            example_board()
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('congratulations! '+player2+ ' has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player1

    if not replay():
        break	
		
		