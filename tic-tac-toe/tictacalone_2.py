import random

import numpy as np
import matplotlib.pyplot as plt

# * GLOBAL VARIABLES *
# int count is used for initializing fivetwelve
# array "fivetwelve" represents every possible TTT combination (given 2 possible cell states, X and blank)
# array "nines" has 512 rows by 9 columns
# lastMove represents the last move taken by the playGame() function
count = 0
fivetwelve = ["" for i in range(512)]
nines = [[0]*9 for i in range(512)]
lastMove = 0

# * GAMEPLAY FUNCTIONS *


def printBoard(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
# helper method: checks to make sure all 3 elements in an array are 'X'


def threeCheck(board, array):
    count = 0
    for i in range(len(array)):
        if board[array[i]] == 'X':
            count = count + 1
    if count == 3:
        return True


def horiCheck(board):

    hwin1 = [0, 1, 2]
    hwin2 = [3, 4, 5]
    hwin3 = [6, 7, 8]

    if threeCheck(board, hwin1):
        return True
    if threeCheck(board, hwin2):
        return True
    if threeCheck(board, hwin3):
        return True
    return False


def vertCheck(board):

    vwin1 = [0, 3, 6]
    vwin2 = [1, 4, 7]
    vwin3 = [2, 5, 8]

    if threeCheck(board, vwin1):
        return True
    if threeCheck(board, vwin2):
        return True
    if threeCheck(board, vwin3):
        return True
    return False


def diagCheck(board):

    dwin1 = [0, 4, 8]
    dwin2 = [2, 4, 6]

    if threeCheck(board, dwin1):
        return True
    if threeCheck(board, dwin2):
        return True
    return False


def resetBoard(board):
    board = ["_" for i in range(9)]
    return board
# if the board has 3 Xs in a row


def gameWon(board):
    if horiCheck(board):
        return True
    if vertCheck(board):
        return True
    if diagCheck(board):
        return True
    return False

# * ARRAY INPUT FUNCTIONS*
# Function to print the output


def printTheArray(arr, n):

    s = ""

    for i in range(0, n):
        s = s + str(arr[i])
        # print(s) // dummied out

    # print(s)

    global count
    global fivetwelve
    fivetwelve[count] = s
    count = count + 1
# Function to generate all binary strings


def generateAllBinaryStrings(n, arr, i):

    if i == n:
        printTheArray(arr, n)
        return

    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)

    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


def initArrays():
    global count
    count = 0
    n = 9
    arr = [None] * n
    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
    # print(count)


def boardBinary(board):
    #print("representing board as binary string:")
    s = ""
    for i in range(9):
        if board[i] == 'X':
            s = s + '1'
        else:
            s = s + '0'
    # print(s)
    return s


def playGame(board):
    global lastMove
    # "moves" will be anywhere from 3 to 6 (wins at < 3 and > 6 are impossible)
    moves = 0
    while gameWon(board) == False:
        action = random.choice(range(9))
        while board[action] == 'X':
            action = random.choice(range(9))
        # print("action: ", action)
        if board[action] != 'X':
            lastMove = action
            board[action] = 'X'
            moves = moves + 1
    #print("New board: ")
    # printBoard(board)
    #print("Total moves: ", moves)
    s = boardBinary(board)
    index512 = fivetwelve.index(s)
    #print("512 index is ", str(index512))
    #print("calcReward: ", calcReward(moves))
    nines[index512][lastMove] = nines[index512][lastMove] + calcReward(moves)
    #print("result: ", nines[index512][7])


def calcReward(moves):
    if moves == 3:
        return 5
    if moves == 4:
        return 4
    if moves == 5:
        return 3
    if moves == 6:
        return 2
    return 1


def main():
    initArrays()

# local variables
    board = ["_" for i in range(9)]
    printBoard(board)

# initialize fivetwelve and nines arrays

    # episodes
    episodes = 10000
    for _ in range(episodes):
        playGame(board)
        board = resetBoard(board)

    print("program complete")
    print(nines)
    plt.imshow(nines, cmap='hot', aspect='auto', interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    main()
