
# this code is a modification of the code at  https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

from termcolor import colored

board = [x for x in range(10)]


def inserstLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == str(pos)


def color(var):
    if var in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return colored(var, 'grey')
    elif var == 'x':
        return colored(var, 'green')
    elif var == 'o':
        return colored(var, 'red')


def printBoard(board):
    print('   |   |  ')
    print(' ' + color(board[1]) + ' | ' + color(board[2]) + ' | ' + color(board[3]))
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' ' + color(board[4]) + ' | ' + color(board[5]) + ' | ' + color(board[6]))
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' ' + color(board[7]) + ' | ' + color(board[8]) + ' | ' + color(board[9]))
    print('   |   |  ')


def isBoardFull(board):
    counter = 0
    for x in board:
        if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            counter = counter + 1

    if counter > 0:
        return False
    else:
        return True


def isWinner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))


def playerMove():
    run = True
    while run:
        move = input("please select a postion to enter the x between 1 and 9: ")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    inserstLetter('x', move)
                else:
                    print("Sorry, This space is occupied")
            else:
                print("Please type a number between 1 and 9")
        except:
            print("Please type a number")


def maxAlphaBeta(alpha, beta):
    # values:
    # win = 1
    # lose = -1
    # tie = 0

    # initialize maxVal with a value smaller than the smallest possible value
    maxVal = -2
    pos = None

    # check if we reach leaf (some one win or tie)
    # x:User    o:AI
    if isWinner(board, 'x'):
        return (-1, 0)
    elif isWinner(board, 'o'):
        return (1, 0)
    elif isBoardFull(board):
        return (0, 0)

    for i in range(1, len(board)):
        if board[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:

            board[i] = 'o'
            m, min_pos = minAlphaBeta(alpha, beta)
            if m > maxVal:
                maxVal = m
                pos = i
            board[i] = str(i)

            if maxVal >= beta:
                return (maxVal, pos)

            if maxVal > alpha:
                alpha = maxVal

    return (maxVal, pos)


def minAlphaBeta(alpha, beta):
    # values:
    # win = 1
    # lose = -1
    # tie = 0

    # initialize minVal with a value larger than the largest possible value
    minVal = 2
    pos = None

    # check if we reach leaf (some one win or tie)
    # x:User    o:AI
    if isWinner(board, 'x'):
        return -1, 0
    elif isWinner(board, 'o'):
        return 1, 0
    elif isBoardFull(board):
        return 0, 0

    for i in range(0, len(board)):
        if board[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:

            board[i] = 'x'
            m, pos = maxAlphaBeta(alpha, beta)
            if m < minVal:
                minVal = m
                pos = i
            board[i] = str(i)

            if minVal <= alpha:
                return minVal, pos

            if minVal < beta:
                beta = minVal

    return minVal, pos


def main():
    print("Welcome to the game")
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'o'):
            playerMove()
            printBoard(board)
            print("----------------------------")
        else:
            print("sorry you loose!")
            break

        if not isWinner(board, 'x'):
            val, move = maxAlphaBeta(-2,2)
            if move == 0:
                print(" ")
            else:
                inserstLetter('o', move)
                print("computer placed an o on position", move, ";")
                printBoard(board)
                print("--------------------------------------")

        else:
            print("you win")
            break

    if isBoardFull(board):
        print("Tie game")


while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [str(x) for x in range(10)]
        print("------------------------")
        main()
    elif x.lower() == 'n':
        break
    else:
        print("Incorrect choice.")
