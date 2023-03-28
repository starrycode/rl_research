# 2. what-actions.py: Given a file describing the state, print out what actions are available to be played
#     1. INPUT: a file describing the state of the board like above
#     2. OUTPUT: A file with a list of actions that can be played next (N,X)
import fileinput

# 0 1 2
# 3 4 5
# 6 7 8

inputFile = open("what-actions.txt", "r")
actions = []

for line in inputFile:
    # print(line)
    location = line.split(",")[0].split('(')[1]  # 4, 0, ...
    player = line.split(",")[1].split(')')[0]  # X, _, ...
    if player == '_':
        actions.append('(' + str(location) + ',X)')

inputFile.close()


outputFile = open("what-actions-out.txt", "w")

for i in range(len(actions)):
    print(actions[i], file=outputFile)

outputFile.close()
