# 4. calc-reward.py:
#     1. INPUT: a file describing the state of the board
#     2. OUTPUT: a file with the number of times that the player has won (how many 3-in-a-rows)

import fileinput
inputFile = open("calc-reward.txt", "r")

board = ['' for x in range(9)]


for line in inputFile:
    # print(line)
    location = line.split(",")[0].split('(')[1]  # 4, 0, ...
    player = line.split(",")[1].split(')')[0]  # X, _, ...
    board[int(location)] = player


def wins():
    winCount = 0
    # check row
    if board[0] == board[1] == board[2] == 'X' \
            or board[3] == board[4] == board[5] == 'X' \
            or board[6] == board[7] == board[8] == 'X':
        winCount += 1

    # check col
    if board[0] == board[3] == board[6] == 'X' \
            or board[1] == board[4] == board[7] == 'X' \
            or board[2] == board[5] == board[8] == 'X':
        winCount += 1

    # check diagnoals
    if board[0] == board[4] == board[8] == 'X' \
            or board[2] == board[4] == board[6] == 'X':
        winCount += 1
    return winCount


inputFile.close()

# outputting the number of times X has won
outputFile = open("calc-reward-out.txt", "w")
print(wins(), file=outputFile)

outputFile.close()
