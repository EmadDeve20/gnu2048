#!/bin/env python3

"""
this is class for handeling keys for playing this Game!
Lets do this :>
we are have Fun Life :D
"""

from readchar import readkey
import push_numbers as p


def true_key(key):

    # ('\x03' = ctr + c) and ('\x1a' = ctr + z ) and ('\x18' = ctr + x)
    if key == 'Q' or key == 'q' or key == '\x03'\
        or key == '\x1a' or key == '\x18': #for quit in the game
        return True

    # '\x1b[A' = top_arrow
    # '\x1b[B' = bot_arrow
    # '\x1b[D' = left_arrow
    # '\x1b[C' = right_arrow

    if key == 'W' or key == 'w'\
        or key == 'K' or key == 'k'\
        or key == '\x1b[A': #for pushing to Up
        return True

    if key == 'S' or key == 's'\
        or key == 'J' or key == 'j'\
        or key == '\x1b[B': #for pushing to Down
        return True

    if key == 'A' or key == 'a'\
        or key == 'H' or key == 'h'\
        or key == '\x1b[D': #for pushing to Left
        return True

    if key == 'D' or key == 'd'\
        or key == 'L' or key == 'l'\
        or key == '\x1b[C': #for pushing to Right
        return True

    return False #if not true char

def controler(mat):
    """this function can controling all true key Events"""
    c = readkey()
    if true_key(c):

        if c == 'Q' or c == 'q' or c == '\x03'\
            or c == '\x1a' or c == '\x18':
            quit()

        if c == 'W' or c == 'w'\
        or c == 'K' or c == 'k'\
        or c == '\x1b[A':
            if p.can_pushing_up(mat):
                p.pushing_up(mat)
                brid_number(mat)

        if c == 'S' or c == 's'\
        or c == 'J' or c == 'j'\
        or c == '\x1b[B':
            if p.can_pushing_down(mat):
                p.pushing_down(mat)
                brid_number(mat)

        if c == 'D' or c == 'd'\
        or c == 'L' or c == 'l'\
        or c == '\x1b[C':
            if p.can_pushing_right(mat):
                p.pushing_right(mat)
                brid_number(mat)

        if c == 'A' or c == 'a'\
        or c == 'H' or c == 'h'\
        or c == '\x1b[D':
            if p.can_pushing_left(mat):
                p.pushing_left(mat)
                brid_number(mat)

def brid_number(mat):
    """this for living Game :D"""
    import random
    random.seed()

    have_zero = False
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                have_zero = True
    while have_zero:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if mat[x][y] == 0:
            mat[x][y] = 2
            have_zero = False
