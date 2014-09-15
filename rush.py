#!/usr/bin/env python
from sys import stdout
#
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#

horiz = {'A':2,'X':2,'C':2}
verti = {'B':2,'O':3,'P':3}

# fail somewhat gracefully

def fail (msg):
    raise StandardError(msg)


GRID_SIZE = 6


def validate_move (board,move):
    car = move[0]
    direc = move[1]
    steps = move[2]
    head = board_loc[car]
    if car in horiz.keys():
        carlen = horiz[car]
    else:
        carlen = verti[car]
    if (direc == 'w' or direc == 's') and car in horiz.keys():
        return False
    elif (direc == 'a' or direc == 'd') and car in verti.keys():
        return False
    if direc == 'w' and head[0] != 0 and steps <= head[0]:
        for i in range(steps):
            if board[head[0] - (i+1)][head[1]] != '.':
                return False
    if direc == 's' and head[0] + (carlen-1) != 5 and steps >= head[0] + (carlen - 1):
        for i in range(steps):
            if board[head[0] + (carlen-1) + (i+1)][head[1]] != '.':
                return False
    if direc == 'a' and head[1] != 0 and steps <= head[1]:
        for i in range(steps):
            if board[head[0]][head[1] - (i+1)] != '.':
                return False
    if direc == 'd' and head[1] + (carlen-1) != 5 and steps >= head[1] + (carlen - 1):
        for i in range(steps):
            if board[head[0]][head[1] + (carlen-1) - (i+1)] != '.':
                return False
    return True




def read_player_input (brd):
    # FIX ME!
    car = raw_input("Please choose a car: ")
    direction = raw_input("Please choose direction(w,a,s,d): ")
    steps = int(raw_input("Please input distance to move: "))
    return (car,direction,steps)


def update_board (board,move):
    if validate_move(board,move):
        oldcar = board_loc[move[0]]
        if move[1] == 'w':
            print board_loc
            print board
            print move
            print type(move[2])
            board_loc[move[0]] = (board_loc[move[0]][0] - (move[2]),board_loc[move[0]][1])
            board[oldcar[0]][oldcar[1]] = '.'
            board[oldcar[0]+1][oldcar[1]] = '.'
            board[board_loc[move[0]][0]][board_loc[move[0]][1]] = move[0]
            board[board_loc[move[0]][0]+1][board_loc[move[0]][1]] = move[0]
            if verti[move[0]] == 3:
                board[oldcar[0]+2][oldcar[1]] = '.'
                board[board_loc[move[0]][0]+2][board_loc[move[0]][1]] = move[0]

        elif move[1] == 's':
            board_loc[move[0]] = (board_loc[move[0]][0] + (move[2]),board_loc[move[0]][1])
            board[oldcar[0]][oldcar[1]] = '.'
            board[oldcar[0]+1][oldcar[1]] = '.'
            board[board_loc[move[0]][0]][board_loc[move[0]][1]] = move[0]
            board[board_loc[move[0]][0]+1][board_loc[move[0]][1]] = move[0]
            if verti[move[0]] == 3:
                board[oldcar[0]+2][oldcar[1]] = '.'
                board[board_loc[move[0]][0]+2][board_loc[move[0]][1]] = move[0]
        elif move[1] == 'a':
            board_loc[move[0]] = (board_loc[move[0]][0],board_loc[move[0]][1] - (move[2]))
            board[oldcar[0]][oldcar[1]] = '.'
            board[oldcar[0]][oldcar[1]+1] = '.'
            board[board_loc[move[0]][0]][board_loc[move[0]][1]] = move[0]
            board[board_loc[move[0]][0]][board_loc[move[0]][1]+1] = move[0]
            if horiz[move[0]] == 3:
                board[oldcar[0]][oldcar[1]+2] = '.'
                board[board_loc[move[0]][0]][board_loc[move[0]][1]+2] = move[0]
        elif move[1] == 'd':
            board_loc[move[0]] = (board_loc[move[0]][0],board_loc[move[0]][1] + (move[2]))
            board[oldcar[0]][oldcar[1]] = '.'
            board[oldcar[0]][oldcar[1]+1] = '.'
            board[board_loc[move[0]][0]][board_loc[move[0]][1]] = move[0]
            board[board_loc[move[0]][0]][board_loc[move[0]][1]+1] = move[0]
            if horiz[move[0]] == 3:
                board[oldcar[0]][oldcar[1]+2] = '.'
                board[board_loc[move[0]][0]][board_loc[move[0]][1]+2] = move[0]


    return board


def print_board (brd):
    i=0
    for x in brd:
        for y in x:
            stdout.write(str(y) + ' ')
        if i == 2:
            stdout.write('==>')
        print("")
        i += 1

    
def done (brd):
    if brd[2][4] == 'X' and brd[2][5] == 'X':
        return True


# initial board:
# Board positions (1-6,1-6), directions 'r' or 'd'
#
# X @ (2,3) r
# A @ (2,4) r
# B @ (2,5) d
# C @ (3,6) r
# O @ (4,3) d
# P @ (6,4) d


def create_initial_level ():
    board = [[None]*6,[None]*6,[None]*6,[None]*6,[None]*6,[None]*6]
    for x in range(6):
        for y in range(6):
            board[x][y] = '.'
    board[2][1] = 'X'
    board[2][2] = 'X'
    board[3][1] = 'A'
    board[3][2] = 'A'
    board[4][1] = 'B'
    board[5][1] = 'B'
    board[5][2] = 'C'
    board[5][3] = 'C'
    board[2][3] = 'O'
    board[3][3] = 'O'
    board[4][3] = 'O'
    board[3][5] = 'P'
    board[4][5] = 'P'
    board[5][5] = 'P'
    return board

board_loc = {'X':(2,1),'A':(3,1),'B':(4,1),'C':(5,2),'O':(2,3),'P':(3,5)}

def main ():

    brd = create_initial_level()

    print_board(brd)

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'
        

if __name__ == '__main__':
    main()
