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



# fail somewhat gracefully

def fail (msg):
    raise StandardError(msg)


GRID_SIZE = 6


def validate_move (brd,move):
    # FIX ME!
    # check that piece is on the board
    # check that piece placed so it can move in that direction
    # check that piece would be in bound
    # check that path to target position is free
    return False


def read_player_input (brd):
    # FIX ME!
    car = raw_input("Please choose a car: ")
    direction = raw_input("Please choose direction(w,a,s,d): ")
    steps = raw_input("Please input distance to move: ")
    return (car,direction,steps)


def update_board (brd,move):
    # FIX ME!
    return brd


def print_board (brd):
    for x in brd:
        for y in x:
            stdout.write(str(y) + ' ')
        print("")

    
def done (brd):
    # FIX ME!
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
