#!/bin/env python3

"""
this is not completed!
i need time for creating better this code or you are can help me with creating better code.
we have a fun life :D
"""

from os import system
from pnum import prmat
from key_manager import controler , brid_number
from saver import saving_record
import push_numbers as p
import platform

class Player:
    """this is class can solve 2048 game"""
    def __init__(self):
        """crated numbers for player"""
        #we need this is numbers for showing and playing
        self.numbers = [[0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0]]

        self.nativ_numbers = [[],[],[],[]]
        # matrix need double this function for first run
        brid_number(self.numbers)
        brid_number(self.numbers)

        self.draw()
    def draw(self):
        """draw play-ground"""
        os_name = platform.system()
        if os_name == "Linux":
            system('clear')
        elif os_name == "Windows":
            system('cls')
        prmat(self.numbers)
        self.print_score_and_record()
        

    def game_manager(self):
        """this function for managing game"""
        while p.matrix_is_alive(self.numbers):
           self.playing_game()
           self.draw()

        print("end Thank You For Using This Game:D")

    def score(self):
        """This is function can calculate the score"""
        result = 0
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] != 2:
                    result += self.numbers[i][j]

        saving_record(result)
        return result

    def print_score_and_record(self):
        """this function can printing score and record for player"""
        print(f"Score: {self.score()} \t Record: {open('.record' , 'r').read()}")
        

    def playing_game(self):
        """i can be playing 2048 game :D"""
        controler(self.numbers)
#if __name__ == '__main__' :
#    player = Player()
#    player.game_manager()
