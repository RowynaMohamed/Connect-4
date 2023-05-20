import numpy as np
import pygame
import sys
import random
import math
from alpha_beta import alpha_beta
from minimax import minimax
from board import Board
from board import checkWinning

from board import checkLocation
from board import getNextRow
from board import putPeace

from board import DrawBoard


def get_col_random():
    c = random.randint(0, 7)
    return c


def play(level,choice):

    GameFinshed = False
    turn = 0
    while GameFinshed == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # take input from player 1
                if turn == 0: # this condition tell us that at turn zero is the player 1
                   if(choice == 1):

                         eval, column =minimax(1, 4)
                   else:
                        eval,column = alpha_beta(1, 4, float('-inf'), float('inf') )

                   if checkLocation(Board, column):
                        row = getNextRow(Board, column)
                        putPeace(Board, row, column, 1)
                        if checkWinning(Board, 1):
                            print("PALYER 1 WINS (-_-) !!!!!!!")
                            GameFinshed = True
                else: #take input from player 2
                        #positionOFx = event.pos[0]
                        while not checkLocation(Board, column):
                            if (level == 2):
                                eval, column = alpha_beta(1, 4, float('-inf'), float('inf'))
                            elif (level == 3):
                                eval, column = minimax(1, 4)
                            else:
                                column = get_col_random()
                                while not checkLocation(Board, column):
                                    column = get_col_random()
                        if checkLocation(Board, column):
                            row = getNextRow(Board, column)
                            putPeace(Board, row, column, 2)
                            if checkWinning(Board, 2):
                                print("PALYER 2 WINS (-_-) !!!!!!!")
                                GameFinshed = True
                print(np.flip(Board, 0))
                DrawBoard(Board)
                turn +=1
                turn = turn % 2 # this is made for changing btween players (1,2)
                if GameFinshed == True:
                    pygame.time.wait(8000)


#play(3,1)