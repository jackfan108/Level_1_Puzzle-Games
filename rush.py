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
    if direc == 'w' and head[0] != 0 and head[0] - steps >= 0:
        for i in range(steps):
            if board[head[0] - (i+1)][head[1]] != '.':
                return False
    elif direc == 's' and head[0] + (carlen-1) != 5 and head[0] + (carlen-1) + steps <=5:
        for i in range(steps):
            if board[head[0] + (carlen-1) + (i+1)][head[1]] != '.':
                return False
    elif direc == 'a' and head[1] != 0 and head[1] - steps >= 0:
        for i in range(steps):
            if board[head[0]][head[1] - (i+1)] != '.':
                return False
    elif direc == 'd' and head[1] + (carlen-1) != 5 and head[1] + (carlen-1) + steps <= 5:
        for i in range(steps):
            if board[head[0]][head[1] + (carlen-1) + (i+1)] != '.':
                return False
    else:
        return False
    return True




def read_player_input (brd):
    # FIX ME!
    not_pass = False
    car = ''
    direc = ''
    steps = 0
    while car not in horiz.keys() and car not in verti.keys():
        car = raw_input("Please choose a car: ")
    while direc not in ['a','w','s','d']:
        direc = raw_input("Please choose direction(w,a,s,d): ")
    while steps <= 0 or steps >=5:
        try:
            steps = int(raw_input("Please input distance to move: "))
        except ValueError:
            print "You done fucked up bitch!"
            pass
    return (car, direc, steps)


def update_board (board,move):
    if validate_move(board,move):
        car = move[0]
        direc = move[1]
        steps = move[2]
        oldcar = board_loc[move[0]]
        oldx = oldcar[0]
        oldy = oldcar[1]

        if direc == 'w':
            board_loc[car] = (board_loc[car][0] - (steps),board_loc[car][1])
            board[oldx][oldy] = '.'
            board[oldx+1][oldy] = '.'
            if verti[car] == 3:
                board[oldx+2][oldy] = '.'
            board[board_loc[car][0]][board_loc[car][1]] = car
            board[board_loc[car][0]+1][board_loc[car][1]] = car
            if verti[car] == 3:
                board[board_loc[car][0]+2][board_loc[car][1]] = car

        elif direc == 's':
            board_loc[car] = (board_loc[car][0] + (steps),board_loc[car][1])
            board[oldx][oldy] = '.'
            board[oldx+1][oldy] = '.'
            if verti[car] == 3:
                board[oldx+2][oldy] = '.'
            board[board_loc[car][0]][board_loc[car][1]] = car
            board[board_loc[car][0]+1][board_loc[car][1]] = car
            if verti[car] == 3:
                board[board_loc[car][0]+2][board_loc[car][1]] = car
        elif direc == 'a':
            board_loc[car] = (board_loc[car][0],board_loc[car][1] - (steps))
            board[oldx][oldy] = '.'
            board[oldx][oldy+1] = '.'
            if horiz[car] == 3:
                board[oldx][oldy+2] = '.'
            board[board_loc[car][0]][board_loc[car][1]] = car
            board[board_loc[car][0]][board_loc[car][1]+1] = car
            if horiz[car] == 3:
                board[board_loc[car][0]][board_loc[car][1]+2] = car
        elif direc == 'd':
            board_loc[car] = (board_loc[car][0],board_loc[car][1] + (steps))
            board[oldx][oldy] = '.'
            board[oldx][oldy+1] = '.'
            if horiz[car] == 3:
                board[oldx][oldy+2] = '.'
            board[board_loc[car][0]][board_loc[car][1]] = car
            board[board_loc[car][0]][board_loc[car][1]+1] = car
            if horiz[car] == 3:
                board[board_loc[car][0]][board_loc[car][1]+2] = car
    else:
        print "You done fuked bitch!"


    return board


def print_board (board):
    i=0
    print board
    for x in board:
        for y in x:
            stdout.write(str(y) + ' ')
        if i == 2:
            stdout.write('==>')
        print("")
        i += 1

    
def done (board):
    if board[2][4] == 'X' and board[2][5] == 'X':
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
