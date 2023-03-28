import fileinput
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import style

finished = 0
q_matrix = np.zeros((512, 9), dtype=int)
emptySpot = '_'
board = [emptySpot for x in range(9)]
winCount = 0
rewards = [-10, 100, 200, 300, 400, 500, 600, 10000]
discount = 0.9
learning_rate = 0.1
# or
# board = np.zeros((3,3))

# row#, col#
# q_matrix[state][action]

# -,-,-,X,-,-,O,-,- | action

# [[0 0 0 0 0 0 0 0 0] q_matrix[][]
# [0 1 0 0 0 0 0 0 0]
# [0 1 0 1 0 0 0 0 0] q_matrix[2][7]
# [0 1 0 1 0 0 0 1 0]
# ]]
# 512 states for either x or open
# 000000000 will be 0 tile filled state

# state, what-actions, play-action, calc-reward (q-learning)

# use randrange to get a rnumber between 0-511
# we should keep track of this rnumber; it will be the row index in q_matrix
# convert that number to binary using:
# binString = "{0:b}".format(DEC_NUMBER_HERE).zfill(9)
# let us use rnum = 9 for now
rnum = 9


def binStringToDec(b_string):
    return int(b_string, 2)


def decToBinString(rnum):
    binString = "{0:b}".format(int(rnum)).zfill(9)
    return binString  # string type


print(type(decToBinString(rnum)))
print(decToBinString(rnum))
print(decToBinString(rnum)[1] == '1')


def getAllPossibleNextAction(binaryState):
    # state = decToBinString(rnum)

    if binaryState == '111111111':
        return 'FULL'
    possibleActions = []
    for i in range(9):
        if binaryState[i] == '0':
            possibleActions.append(i)
    return possibleActions


def chooseAction(binaryState):  # Choose an action to play
    # TODO: choose a random action in the empty spots

    action = random.choice(getAllPossibleNextAction(binaryState))
    return action


def getNextState(cur_state, action):
    # TODO: modify cur_state
    # while using the index = action - 1
    # in that index, change the char to 1
    # and return that as a new_state
    replacement_char = '1'
    nextState = cur_state[:action] + replacement_char + cur_state[action+1:]
    return nextState


binState = decToBinString(rnum)
print(getNextState(binState, chooseAction(binState)))
print("=======")


def play_game():
    # finishied will be 1 when it reaches the goal state (=one 3-in-a-row)

    # Give it a random state (between 0 and 511)
    # Current state is randomly chosen
    cur_state = 0
    # random.randrange(512)
    while True:
        b_state = decToBinString(cur_state)
        possible_actions = getAllPossibleNextAction(b_state)

        if possible_actions == 'FULL':
            break
        action = random.choice(possible_actions)  # this will be decimal
        next_b_state = getNextState(b_state, action)

        # convert next_state back to dec so we can use it as an index
        next_state = eval('0b' + next_b_state)
        print('action:', action)

        q_matrix[cur_state][action] = q_matrix[cur_state][action] + learning_rate * \
            (rewards[numOfWins(cur_state)] + discount *
             max(q_matrix[next_state]) - q_matrix[cur_state][action])

        cur_state = next_state
        next_b_state = decToBinString(cur_state)

        if numOfWins(next_b_state) > 0:
            print('numOfWins', numOfWins(cur_state))
            print("It won")
            break
    print("Episode ", _, " done")


print(q_matrix)
print("Training done...")
# fill the q-table

# checking for reward (how many 3-in-a-rows)
# Check if there's a 3-in-a-row


def numOfWins(i_state):
    winCount = 0
    state = decToBinString(i_state)
    # check row
    if state[0] == state[1] == state[2] == '1':
        winCount += 1
    if state[3] == state[4] == state[5] == '1':
        winCount += 1
    if state[6] == state[7] == state[8] == '1':
        winCount += 1

    # check col
    if state[0] == state[3] == state[6] == '1':
        winCount += 1
    if state[1] == state[4] == state[7] == '1':
        winCount += 1
    if state[2] == state[5] == state[8] == '1':
        winCount += 1

    # check diagnoals
    if state[0] == state[4] == state[8] == '1':
        winCount += 1
    if state[2] == state[4] == state[6] == '1':
        winCount += 1
    return winCount


print('*******')
print(numOfWins('111111101'))

for _ in range(2000):  # TODO: Include this later (we'll be testing 1000 cases for now)
    play_game()

print(q_matrix)
outputFile = open("q_matrix.txt", "w")


for i in range(len(q_matrix)):
    print(q_matrix[i], file=outputFile)

outputFile.close()


# style.use('ggplot')


# def get_q_color(value, vals):
#     if value == max(vals):
#         return "green", 1.0
#     else:
#         return "red", 0.3


# fig = plt.figure(figsize=(512, 9))

# ax1 = fig.add_subplot(513)

# i = 2000  # number of iterations

# for x, x_vals in enumerate(q_matrix):
#     for y, y_vals in enumerate(x_vals):
#         ax1.scatter(x, y, c=get_q_color(y_vals[0], y_vals)[
#                     0], marker="o", alpha=get_q_color(y_vals[0], y_vals)[1])

#         ax1.set_ylabel("Action 0")

# plt.show()
# plt.savefig(f"qtable_charts/{i}.png")
# plt.clf()
plt.imshow(q_matrix, cmap='hot', aspect='auto', interpolation='nearest')
plt.show()
