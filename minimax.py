import numpy as np
import pygame
import sys
import random
import math
import constant
from constant import Rows ,Columns ,WIN ,DRAW ,LOSS ,Blue ,Red,Yellow,Black
import board
from board import Board
from board import checkWinning

from board import checkLocation
from alpha_beta import evaluate_state




def make_move(player, col):
    for row in range(Rows):
        if Board[row][col] == 0:
            Board[row][col] = player
            return

# Define the function to undo a move
def undo_move(col):
    for row in range(Rows - 1, -1, -1):
        if Board[row][col] != 0:
            Board[row][col] = 0
            return


def minimax(player, depth):
    if checkWinning(Board, 1) or depth == 0:
        return evaluate_state(), None

    if player == 1:
        best_value = -float('inf')
        best_col = None
        for col in range(Columns):
            if checkLocation(Board, col):
                make_move(1, col)
                value, _ = minimax(2, depth - 1)
                undo_move(col)
                if value > best_value:
                    best_value = value
                    best_col = col
        return best_value, best_col

    else:
        best_value = float('inf')
        best_col = None
        for col in range(Columns):
            if checkLocation(Board, col):
                make_move(2, col)
                value, _ = minimax(1, depth - 1)
                undo_move(col)
                if value < best_value:
                    best_value = value
                    best_col = col
        return best_value, best_col

