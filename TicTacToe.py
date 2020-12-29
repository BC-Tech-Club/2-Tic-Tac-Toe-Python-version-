# This class contains the gameloop of the Tic-Tac-Toe game and uses its
# findBestMove, minimax, and evaluation functions to find the best moves
# for the computer to make. 
from GameBoard import GameBoard
import math

class TicTacToe:
    # constructor
    def __init(self):
        # instantiate a GameBoard object and create 1 or 2 arrays to
        # keep track of the state of the board
        pass

    # captures the user's choice, validates and updates the GameBoard.
    def playerTurn(self):
        pass

    # the computer's turn to play a move
    def compTurn(self):
        pass

    # prints to the command line the end-state of the game and exits the game
    def winner(self):
        pass

    # returns the best move for the computer found using a backtracking
    # algorithm called Minimax.
    def findBestMove(self):
        pass

    # a recursive function that uses a backtracking algorithm to find the highest
    # evaluation for the given gameboard object. The highest evaluation is
    # returned.
    def minimax(self):
        pass

    # checks if each player's chosen positions constitutes a win or not
    def evaluate(self):
        pass

    # mainloop for the game
    def startGame(self):
        pass
