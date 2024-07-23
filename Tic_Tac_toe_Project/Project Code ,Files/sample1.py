board =[' ' for x in range(10)]

def insertMark(mark, pos):
    board[pos] = insert

def printBoard(board):
    # row 1
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('---------------------')

    # row 2
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('---------------------')

    # row 3
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')
    print('---------------------')

def isSpaceFree(pos):
    return (board[pos]==' ')
def isBoardFull(board):
    if board.count(' ')>=1:
        return(False)
    else:
        return(True)

def iswinner(board,letter):
    return((board[1] == letter and board[2] == letter and board[3] == letter) or
           (board[4] == letter and board[5] == letter and board[6] == letter) or
           (board[7] == letter and board[8] == letter and board[9] == letter) or
           (board[1] == letter and board[4] == letter and board[7] == letter) or
           (board[2] == letter and board[5] == letter and board[8] == letter) or
           (board[3] == letter and board[6] == letter and board[9] == letter) or
           (board[1] == letter and board[5] == letter and board[9] == letter) or
           (board[3] == letter and board[5] == letter and board[7] == letter))

if board[1] == letter:
    if board[2] == let