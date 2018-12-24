the_board = {'(1,1)': ' ', '(1,2)': ' ', '(1,3)': ' ',
             '(2,1)': ' ', '(2,2)': ' ', '(2,3)': ' ',
             '(3,1)': ' ', '(3,2)': ' ', '(3,3)': ' ',}

def display(board):
    var = list(board.values())  # Iterator to print out the table
    maxi = len(var)
    for i in range(0, maxi, 3):
        for j in range(i, (i+3)):
            print(var[j], end="")
            if j < i+2:
                print('|', end='')
        print()
        if i < (maxi-1):
            print("-+-+-")

def check(board):
    result = False
    var = board.values
    check = ''
    for i in range(0,3):    # Check if there's a victory horizontally.
        for j in range(i*3,i+3):
            check = var[j]
            if c

turn = 'X'
for k in range(9):
    while True:
        display(the_board)
        print('Turn for '+ turn + '. Move on which space?')
        move = input()
        if move not in the_board:
            print('Error.\nPlease input a valid move.\n')
            continue
        the_board[move] = turn
        break
    turn = 'O' if turn == 'X' else 'X'
display(the_board)
                
