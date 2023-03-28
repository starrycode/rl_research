# 3. play-action.py:
# INPUT: two files, the state of the board, and a file with one action to be played
# OUTPUT: a file describe the new state of the board after the action has been played

emptySpot = '_'
board = [emptySpot for x in range(9)]

boardFileName = input("What is the state of board filename?\n")

boardFile = open(boardFileName, "r")

actionFileName = input("What is the action filename?\n")

actionFile = open(actionFileName, "r")

# Reads each line of file


def playAction(line):
    splitLine = line.strip('()\n').split(',')
    if(board[int(splitLine[0])] == emptySpot):
        board[int(splitLine[0])] = splitLine[1]


for line in boardFile:
    if(line.startswith('#')):
        continue

    playAction(line)

playAction(actionFile.readline())

actionFile.close()
boardFile.close()

outputFile = open("play-action-out.txt", "w")

for i in range(9):
    print(f"({i},{board[i]})", file=outputFile)

outputFile.close()

