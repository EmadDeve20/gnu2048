#!/bin/env python3

""" we need the matrix :D
    i was used in the movie The Matrix in 2002
    im not a liar :^)
"""


def can_pushing_left(mat):
    """this is function can checking for we can pushing numbers to the left or not"""
    for i in range(len(mat)):
        # checks whether equal numbers are next to each other in the matrix
        # either there is empty space or not
        # if not, the matrix can not be pushing numbers to left
        for j in range(len(mat)-1 , 0 , -1):
            if mat[i][j] == mat[i][j-1] and mat[i][j] != 0:
                return True
            if mat[i][j] != 0 and mat[i][j-1] == 0:
                return True
    # If matrix can not pushing numbers to left, this function returning False
    return False

def pushing_left(mat):
    """this is function can pushing the matrix to left"""
    #first, pressing matrix in left if can
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1 , 0 , -1):
                    if mat[i][j] != 0 and mat[i][j-1] == 0:
                        mat[i][j-1] = mat[i][j]
                        mat[i][j] = 0
                        j -= 1

                for j in range(len(mat)):
                    if mat[i][j] == 0:
                        i -= 1
                        break

    #second, the integration of matrix numbers
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                if mat[i][j-1] == 0 and j-1 != -1:
                    mat[i][j-1] = mat[i][j]
                    mat[i][j] = 0

    #and in the last review of the correctness of the work of pushing
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1 , 0 , -1):
                    if mat[i][j] != 0 and mat[i][j-1] == 0:
                        mat[i][j-1] = mat[i][j]
                        mat[i][j] = 0
                        j -= 1

                for j in range(len(mat)):
                    if mat[i][j] == 0:
                        i -= 1
                        break


def can_pushing_right(mat):
    """this is function can checking for we can pushing numbers to the right or not"""
    for i in range(len(mat)):
        # checks whether equal numbers are next to each other in the matrix
        # either there is empty space or not
        # if not, matrix can not pushing numbers to left
        for j in range(len(mat)-1 , 0 , -1):
            if mat[i][j] == mat[i][j-1] and mat[i][j] != 0:
                return True
            if mat[i][j-1] != 0 and mat[i][j] == 0:
                return True
    # If matrix can not pushing numbers to right, this function returning False
    return False

def pushing_right(mat):
    """this is function can pushing the matrix to right"""
    #first, pressing matrix in right if can
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1):
                    if mat[i][j] != 0 and mat[i][j+1] == 0:
                        mat[i][j+1] = mat[i][j]
                        mat[i][j] = 0
                        j += 1

                for j in range(len(mat)):
                    if mat[i][j] == 0:
                        i -= 1
                        break

    #second, the integration of matrix numbers
    for i in range(len(mat)):
        for j in range(len(mat)-1 , 0 , -1):
            if mat[i][j] == mat[i][j-1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j-1] = 0

    #And in the last review of the correctness of the work of pushing
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1):
                    if mat[i][j] != 0 and mat[i][j+1] == 0:
                        mat[i][j+1] = mat[i][j]
                        mat[i][j] = 0
                        j += 1

                for j in range(len(mat)):
                    if mat[i][j] == 0:
                        i -= 1
                        break


def can_pushing_up(mat):
    """this is function can checking for we can pushing numbers to the up or not"""
    for i in range(len(mat)):
        for j in range(len(mat)-1 , 0 , -1):
            # checks whether equal numbers are next to each other in the matrix
            # either there is empty space or not
            # just focusing and reading you can read this code i know :D
            if mat[j][i] == mat[j-1][i] and mat[j][i] != 0:
                return True
            if mat[j][i] != 0 and mat[j-1][i] == 0:
                return True
    return False

def pushing_up(mat):
    """this is function can pushing the matrix up"""
    #first, pressing matrix on top of the can
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1,0,-1):
                    if mat[j][i] != 0 and mat[j-1][i] == 0:
                        mat[j-1][i] = mat[j][i]
                        mat[j][i] = 0
                        j -= 1

                for j in range(len(mat)):
                    if mat[j][i] == 0:
                        i += 1
                        break

    #second, the integration of matrix numbers
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if mat[j][i] == mat[j+1][i] and mat[j][i] != 0:
                mat[j][i] *= 2
                mat[j+1][i] = 0

    #And in the last review of the correctness of the work of pushing
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1,0,-1):
                    if mat[j][i] != 0 and mat[j-1][i] == 0:
                        mat[j-1][i] = mat[j][i]
                        mat[j][i] = 0
                        j -= 1

                for j in range(len(mat)):
                    if mat[j][i] == 0:
                        i += 1
                        break


def can_pushing_down(mat):
    """this is function can checking for we can pushing numbers to the down or not"""
    # I think now You can reading this function and no need any comment :D
    for i in range(len(mat)):
        for j in range(0 , len(mat)-1 , 1):
            if mat[j][i] == mat[j+1][i] and mat[j][i] != 0:
                return True
            if mat[j][i] != 0 and mat[j+1][i] == 0:
                return True
    return False

def pushing_down(mat):
    """this is function can pushing the matrix down"""
    #first, press the matrix down
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1):
                    if mat[j][i] != 0 and mat[j+1][i] == 0:
                        mat[j+1][i] = mat[j][i]
                        mat[j][i] = 0
                        j += 1

                for j in range(len(mat)):
                    if mat[j][i] == 0:
                        i -= 1
                        break

    #second, the integration of matrix numbers
    for i in range(len(mat)):
        for j in range(len(mat)-1,0,-1):
            if mat[j][i] == mat[j-1][i] and mat[j][i] != 0:
                mat[j][i] *= 2
                mat[j-1][i] = 0

    #and in the last review of the correctness of the work of pushing
    for count in range(len(mat)-1):
        for i in range(len(mat)):
                for j in range(len(mat)-1):
                    if mat[j][i] != 0 and mat[j+1][i] == 0:
                        mat[j+1][i] = mat[j][i]
                        mat[j][i] = 0
                        j += 1

                for j in range(len(mat)):
                    if mat[j][i] == 0:
                        i -= 1
                        break

def matrix_is_alive(mat):
    """This function can check whether the matrix is alive or not"""

    if can_pushing_down(mat) or can_pushing_up(mat)\
        or can_pushing_left(mat) or can_pushing_right(mat):
        return True

    else:
        return False
