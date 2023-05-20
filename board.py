import constant
from constant import Rows ,Columns ,WIN ,DRAW ,LOSS ,Blue ,Red,Yellow,Black

import numpy as np
import pygame
import sys
import random
import math

def BuildBoard():
    # creating a matrix with 6 rows and 7 columns.(6x7 matrix)
    board = np.zeros((Rows, Columns))
    return board



def putPeace(Board, Row, Column, Piece): #function to put the pieces in the board
    Board[Row][Column] = Piece

def checkLocation(Board, column): # function to check if the location is valid or not
    return Board[5][column] == 0 # if the first row (5) is empty its a valid location

def getNextRow(Board, column):
    for n in range(Rows):
        if Board[n][column] == 0:
            return n

def checkWinning(Board , lastPieceDropped):
    #check the horizontal locations
    for col in range(Columns-3):
        for ro in range(Rows):
            if Board[ro][col] == lastPieceDropped and Board[ro][col+1] == lastPieceDropped and Board[ro][col +2] == lastPieceDropped and Board[ro][col +3] == lastPieceDropped:
                return True
    #check vrtical locations
    for col in range(Columns):
        for ro in range(Rows-3):
            if Board[ro][col] == lastPieceDropped and Board[ro+1][col] == lastPieceDropped and Board[ro+2][col] == lastPieceDropped and Board[ro+3][col] == lastPieceDropped:
                return True
    #check for the right diagonals
    for col in range(Columns-3):
        for ro in range(Rows-3):
            if Board[ro][col] == lastPieceDropped and Board[ro+1][col+1] == lastPieceDropped and Board[ro+2][col+2] == lastPieceDropped and Board[ro+3][col+3] == lastPieceDropped:
                return True
    #check for left diagonals
    for col in range(Columns-3):
        for ro in range(3,Rows):
            if Board[ro][col] == lastPieceDropped and Board[ro-1][col+1] == lastPieceDropped and Board[ro-2][col+2] == lastPieceDropped and Board[ro-3][col+3] == lastPieceDropped:
                return True

def DrawBoard(Board):
    for col in range(Columns):
        for ro in range(Rows):
            pygame.draw.rect(Screen, Blue, (col*SquareSize, ro*SquareSize +SquareSize, SquareSize, SquareSize))
            pygame.draw.circle(Screen, Black, (int(col*SquareSize+SquareSize/2), int(ro*SquareSize+SquareSize+SquareSize/2)), Radius)
    for col in range(Columns):
        for ro in range (Rows):
            if Board[ro][col] == 1:
                pygame.draw.circle(Screen, Red, (int(col*SquareSize+SquareSize/2), height - int(ro*SquareSize+SquareSize/2)), Radius)
            elif Board[ro][col] == 2:
                pygame.draw.circle(Screen, Yellow, (int(col*SquareSize+SquareSize/2), height - int(ro*SquareSize+SquareSize/2)), Radius)
    pygame.display.update()


#intializing a game board (all matrix values start with zero.
Board = BuildBoard()
print(Board)
GameFinshed = False
turn = 0
#create the interface
pygame.init()
SquareSize = 100
width = Columns*SquareSize
height = (Rows+1)*SquareSize
Radius = int (SquareSize/2 -5)
Size = (width, height)
Screen = pygame.display.set_mode(Size)
DrawBoard(Board)
pygame.display.update()
