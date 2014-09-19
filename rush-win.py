#!/usr/bin/env python
from sys import stdout
from graphics import *
#
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#
# initial brd:
# brd positions (1-6,1-6), directions 'r' or 'd'
#
# X @ (2,3) r
# A @ (2,4) r
# B @ (2,5) d
# C @ (3,6) r
# O @ (4,3) d
# P @ (6,4) d

# fail somewhat gracefully
len2 = {'A','B','C','D','E','F','G','H','I','J','K','X'}
len3 = {'O','P','Q','R'}
horiz = {'A','X','C'}
verti = {'B','O','P'}
board_loc = {'X':(2,1),'A':(3,1),'B':(4,1),'C':(5,2),'O':(2,3),'P':(3,5)}
brd = [[None]*6,[None]*6,[None]*6,[None]*6,[None]*6,[None]*6]
rectlist = [[None]*6,[None]*6,[None]*6,[None]*6,[None]*6,[None]*6]
carlist = []

def fail (msg):
    raise StandardError(msg)

def validate_move (brd,move):
    car = move[0]
    direc = move[1]
    steps = move[2]
    head = board_loc[car]
    if car in len2:
        carlen = 2
    else:
        carlen = 3
    if (direc == 'w' or direc == 's') and car in horiz:
        return False
    elif (direc == 'a' or direc == 'd') and car in verti:
        return False
    if direc == 'w' and head[0] != 0 and head[0] - steps >= 0:
        for i in range(steps):
            if brd[head[0] - (i+1)][head[1]] != '.':
                return False
    elif direc == 's' and head[0] + (carlen-1) != 5 and head[0] + (carlen-1) + steps <=5:
        for i in range(steps):
            if brd[head[0] + (carlen-1) + (i+1)][head[1]] != '.':
                return False
    elif direc == 'a' and head[1] != 0 and head[1] - steps >= 0:
        for i in range(steps):
            if brd[head[0]][head[1] - (i+1)] != '.':
                return False
    elif direc == 'd' and head[1] + (carlen-1) != 5 and head[1] + (carlen-1) + steps <= 5:
        for i in range(steps):
            if brd[head[0]][head[1] + (carlen-1) + (i+1)] != '.':
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
    while car.upper() not in horiz and car not in verti:        
        car = raw_input("Please choose a car: ").upper()
    while direc not in ['a','w','s','d']:
        direc = raw_input("Please choose direction(w,a,s,d): ")
    while steps <= 0 or steps >=5:
        try:
            steps = int(raw_input("Please input distance to move: "))
        except ValueError:
            print "You done fucked up bitch!"
            pass
    return (car, direc, steps)

def update_board (brd,move):
    if validate_move(brd,move):
        car = move[0]
        direc = move[1]
        steps = move[2]
        oldcar = board_loc[move[0]]
        oldx = oldcar[0]
        oldy = oldcar[1]

        if direc == 'w':
            board_loc[car] = (board_loc[car][0] - (steps),board_loc[car][1])
            brd[oldx][oldy] = '.'
            brd[oldx+1][oldy] = '.'
            if car in len3:
                brd[oldx+2][oldy] = '.'
            brd[board_loc[car][0]][board_loc[car][1]] = car
            brd[board_loc[car][0]+1][board_loc[car][1]] = car
            if car in len3:
                brd[board_loc[car][0]+2][board_loc[car][1]] = car

        elif direc == 's':
            board_loc[car] = (board_loc[car][0] + (steps),board_loc[car][1])
            brd[oldx][oldy] = '.'
            brd[oldx+1][oldy] = '.'
            if car in len3:
                brd[oldx+2][oldy] = '.'
            brd[board_loc[car][0]][board_loc[car][1]] = car
            brd[board_loc[car][0]+1][board_loc[car][1]] = car
            if car in len3:
                brd[board_loc[car][0]+2][board_loc[car][1]] = car
        elif direc == 'a':
            board_loc[car] = (board_loc[car][0],board_loc[car][1] - (steps))
            brd[oldx][oldy] = '.'
            brd[oldx][oldy+1] = '.'
            if car in len3:
                brd[oldx][oldy+2] = '.'
            brd[board_loc[car][0]][board_loc[car][1]] = car
            brd[board_loc[car][0]][board_loc[car][1]+1] = car
            if car in len3:
                brd[board_loc[car][0]][board_loc[car][1]+2] = car
        elif direc == 'd':
            board_loc[car] = (board_loc[car][0],board_loc[car][1] + (steps))
            brd[oldx][oldy] = '.'
            brd[oldx][oldy+1] = '.'
            if car in len3:
                brd[oldx][oldy+2] = '.'
            brd[board_loc[car][0]][board_loc[car][1]] = car
            brd[board_loc[car][0]][board_loc[car][1]+1] = car
            if car in len3:
                brd[board_loc[car][0]][board_loc[car][1]+2] = car
    else:
        print "You done fuked bitch!"


    return brd

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



def create_initial_level (brd):
    for x in range(6):
        for y in range(6):
            brd[x][y] = '.'
    for i in horiz:
        brd[board_loc[i][0]][board_loc[i][1]] = i
        brd[board_loc[i][0]][board_loc[i][1]+1] = i
        if i in len3:
            brd[board_loc[i][0]][board_loc[i][1]+2] = i
    for i in verti:
        brd[board_loc[i][0]][board_loc[i][1]] = i
        brd[board_loc[i][0]+1][board_loc[i][1]] = i
        if i in len3:
            brd[board_loc[i][0]+2][board_loc[i][1]] = i
    return brd

def change_board(info):
    global horiz, verti, board_loc
    horiz = set()
    verti = set()
    for i in range(len(info)/4):
        board_loc[info[i*4]] = (int(info[i*4+2])-1,int(info[i*4+1])-1)
        if info[i*4 + 3] == 'd':
            verti.add(info[i*4])
        else:
            horiz.add(info[i*4])

def draw_empty_brd(brd,window):
    for i in range(6):
        for k in range(6):
            rectlist[i][k] = Rectangle(Point(10+i*110,10+k*110),Point(110+i*110,110+k*110))
            rectlist[i][k].setOutline('black')
            rectlist[i][k].draw(window)

def draw_car_init(brd,window):
    for i in board_loc:
        headx = board_loc[i][0]
        heady = board_loc[i][1]
        if i in verti and i in len2:
            tailx = board_loc[i][0]+1
            taily = board_loc[i][1]
        elif i in verti and i in len3:
            tailx = board_loc[i][0]+2
            taily = board_loc[i][1]
        elif i in horiz and i in len2:
            tailx = board_loc[i][0]
            taily = board_loc[i][1]+1
        elif i in horiz and i in len3:
            tailx = board_loc[i][0]
            taily = board_loc[i][1]+2
        carp1 = rectlist[heady][headx].getP1()
        carp2 = rectlist[taily][tailx].getP2()
        carlist.append(Rectangle(carp1,carp2))
    for k in carlist:
        k.setFill('red')
        k.draw(window)


def main ():
    global brd
    window = GraphWin('Rush Hour', 670, 670)
    window.setBackground('white')
    brd = create_initial_level(brd)
    print_board(brd)
    draw_empty_brd(brd,window)
    draw_car_init(brd,window)
    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)
    window.close()
    print 'You lucky bastard! Try the next level =D\n'
        

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        change_board(sys.argv[1])
    main()