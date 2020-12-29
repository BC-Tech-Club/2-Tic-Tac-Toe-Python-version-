# This class is used for visualizing the game-states of the Tic Tac Toe game.
# A GameBoard object will be initialized in the constructor of the TicTacToe
# class.
class GameBoard:
    # GameBoard constructor
    def __init__(self):
        self.board = self.createBoard()

    # returns a 2D gameboard using Chars or Strings
    def createBoard(self):
        pass

    # returns a list of tuples that indicate the (row, column)
    # indices that will be changed when a player/computer makes
    # a move
    def getMovePositions(self):
        pass

    # changes the Chars or Strings in move_positions to the values
    # 0 - 8. These are the values the player will enter to indicate
    # which position they'd like to play.
    def fillEmpty(self):
        pass

    # updates the 2D array with the new move
    def playMove(self , pos, symbol):
        pass

    # updates the 2D array by removing the move at the given position
    def undoMove(self , pos, symbol):
        pass

    # returns true if there are moves left to be play, false otherwise
    def isMovesLeft(self):
        pass

    # print the state of the board
    def printBoard(self):
        pass
