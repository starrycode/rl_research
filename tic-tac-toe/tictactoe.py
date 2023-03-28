import fileinput

# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

base = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
inputFile = open("tictactoe.txt", "r")
game = 1  # If game ends, change this to 0
moves = 0
draw = 0
X_wins = 0
O_wins = 0
inconclusive = 0


def updateBase(player, row, col):
    base[row][col] = player


def wins(player):
    # check row
    for i in range(3):
        win = True
        for j in range(3):
            if base[i][j] != player:
                win = False
                break
        if win:
            return win
    # check col
    for i in range(3):
        win = True
        for j in range(3):
            if base[j][i] != player:
                win = False
                break
        if win:
            return win

    # check diagnoals
    win = True
    for i in range(3):
        if base[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(3):
        if base[i][2 - i] != player:
            win = False
            break
    if win:
        return win
    return False


for line in inputFile:
    if line[0] != '#':
        moves += 1
        print(line)
        player = line.split(" ")[0]
        row = int(line.split(" ")[1])
        col = int(line.split(" ")[2])
        updateBase(player, row, col)
        if wins(player):
            print(player, "WINS!")
            if player == 'X':
                X_wins += 1
            else:
                O_wins += 1
            moves = 0
            game = 0
            base = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        if moves == 9:
            print("DRAWS!")
            draw += 1
            moves = 0
            base = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
if game == 0 and moves > 0:
    inconclusive += 1


print(base)
print("X wins:", X_wins)
print("O wins:", O_wins)
print("Draws:", draw)
print("Inconclusive:", inconclusive)
inputFile.close()
