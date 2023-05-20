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
# player 1 is the red one also its the agent
# player 2 is the computer yellow one

def alpha_beta(player, depth, alpha, beta):
    if checkWinning(Board, 1) or depth == 0:
        return evaluate_state(), None

    if player == 1:
        best_value = -float('inf')
        best_col = None
        for col in range(Columns):
            if checkLocation(Board, col):
                make_move(1, col)
                value, _ = alpha_beta(2, depth - 1, alpha, beta)
                undo_move(col)
                if value > best_value:
                    best_value = value
                    best_col = col
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
        return best_value, best_col

    else:
        best_value = float('inf')
        best_col = None
        for col in range(Columns):
            if checkLocation(Board, col):
                make_move(1, col)
                value, _ = alpha_beta(1, depth - 1, alpha, beta)
                undo_move(col)
                if value < best_value:
                    best_value = value
                    best_col = col
                beta = min(beta, best_value)
                if alpha >= beta:
                    break
        return best_value, best_col


# Define the function to evaluate the utility of a state
def evaluate_state():
    # Check for a horizontal win
    for row in range(Rows):
        for col in range(Columns - 3):
            if Board[row][col] == Board[row][col + 1] == Board[row][col + 2] == Board[row][col + 3] == 1:
                return WIN
            elif Board[row][col] == Board[row][col + 1] == Board[row][col + 2] == Board[row][col + 3] == 2:
                return LOSS

    # Check for a vertical win
    for row in range(Rows - 3):
        for col in range(Columns):
            if Board[row][col] == Board[row + 1][col] == Board[row + 2][col] == Board[row + 3][col] == 1:
                return WIN
            elif Board[row][col] == Board[row + 1][col] == Board[row + 2][col] == Board[row + 3][col] == 2:
                return LOSS

    # Check for a diagonal win (top-left to bottom-right)
    for row in range(Rows - 3):
        for col in range(Columns - 3):
            if Board[row][col] == Board[row + 1][col + 1] == Board[row + 2][col + 2] == Board[row + 3][col + 3] == 1:
                return WIN
            elif Board[row][col] == Board[row + 1][col + 1] == Board[row + 2][col + 2] == Board[row + 3][col + 3] == 2:
                return LOSS

    # Check for a diagonal win (bottom-left to top-right)
    for row in range(3, Rows):
        for col in range(Columns - 3):
            if Board[row][col] == Board[row - 1][col + 1] == Board[row - 2][col + 2] == Board[row - 3][col + 3] == 1:
                return WIN
            elif Board[row][col] == Board[row - 1][col + 1] == Board[row - 2][col + 2] == Board[row - 3][col + 3] == 2:
                return LOSS

    # No winner yet
    return DRAW

#####################