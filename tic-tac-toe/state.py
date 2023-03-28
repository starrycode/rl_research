# 1. state.py: given a file with a list of the actions played, produce a file that describes the state 
# INPUT: a file with a list of actions played of the form (N, X) where N is a position from 0-8
# OUTPUT: a file describing the state of the board with 9 pairs of values of the form (N,P) where N is the position (0-8) and P is what is placed there (X or __ ) 

emptySpot = '_'
board = [emptySpot for x in range(9)]

fileName = input("What is the filename?\n")

inputFile = open(fileName, "r")

# Reads each line of file
for line in inputFile:
    if(line.startswith('#')):
        continue
    
    splitLine = line.strip('()\n').split(',')
    if(board[int(splitLine[0])] == emptySpot):
        board[int(splitLine[0])] = splitLine[1]
    
inputFile.close()

outputFile = open("state-output.txt", "w")


for i in range(9):
    print(f"({i},{board[i]})", file = outputFile)
    
outputFile.close()
    

    