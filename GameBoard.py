# This class is used for visualizing the game-states of the Tic Tac Toe game.
# A GameBoard object will be initialized in the constructor of the TicTacToe
# class.
class GameBoard:
    # GameBoard constructor
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        # returns a 2D gameboard using Chars or Strings
        pass

    def getMovePositions(self):
        # returns a list of tuples that indicate the (row, column)
        # indices that will be changed when a player/computer makes
        # a move
        pass

    def fillEmpty(self):
        # changes the Chars or Strings in move_positions to the values
        # 0 - 8. These are the values the player will enter to indicate
        # which position they'd like to play.
        pass

    def printBoard(self):
        # print the state of the board
        pass
