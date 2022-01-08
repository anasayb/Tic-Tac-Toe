import random
from termcolor import colored

board = [x for x in range(10)]


def inserstLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == str(pos)


def color(var):

    if var in ['1','2','3','4','5','6','7','8','9']:
        return colored(var,'grey')
    elif var== 'x':
        return colored(var,'red')
    elif var == 'o':
        return colored(var,'green')


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
    counter =0
    for x in board:
        if x in ['1','2','3','4','5','6','7','8','9']:
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
                    inserstLetter('x',move)
                else:
                    print("Sorry, This space is occupied")
            else:
                print("Please type a number between 1 and 9")
        except:
            print("Please type a number")



def computerMove(board):

    possilbeMoves = [x for x,letter in enumerate(board) if letter == str(x) and x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possilbeMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possilbeMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = random.choice(cornersOpen)
        return move

    if 5 in possilbeMoves:
        move = 5
        return move

    edgeOpen = []
    for i in possilbeMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)

    if len(edgeOpen) > 0:
        move = random.choice(edgeOpen)
        return move

    return move


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

        if not isWinner(board,'x'):
            move = computerMove(board)
            if move == 0:
                print(" ")
            else:
                inserstLetter('o', move)
                printBoard(board)
                print("computer placed an o on position", move, ";")
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

