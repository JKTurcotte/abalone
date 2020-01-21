from typing import Any
import random


class game:

    def __init__(self, setUp, capturedToWin):
        self.setUp = setUp
        self.capturedToWin = capturedToWin
        self.turn = 2
        self.board = [[4, 4, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4, 4, 4, 4],
                     [4, 4, 4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4, 4, 4],
                     [4, 4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4, 4],
                     [4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4],
                     [3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3],
                     [4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4],
                     [4, 4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4, 4],
                     [4, 4, 4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4, 4, 4],
                     [4, 4, 4, 4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4]]

    def setUpDefault(self):
        self.board = [[4, 4, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4],
                      [4, 4, 4, 4, 3, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 3, 4, 4, 4, 4],
                      [4, 4, 4, 3, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 3, 4, 4, 4],
                      [4, 4, 3, 4, 0, 4, 0, 4, 1, 4, 1, 4, 1, 4, 0, 4, 0, 4, 3, 4, 4],
                      [4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4],
                      [3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3],
                      [4, 3, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 3, 4],
                      [4, 4, 3, 4, 0, 4, 0, 4, 2, 4, 2, 4, 2, 4, 0, 4, 0, 4, 3, 4, 4],
                      [4, 4, 4, 3, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 3, 4, 4, 4],
                      [4, 4, 4, 4, 3, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 3, 4, 4, 4, 4],
                      [4, 4, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4]]

    def move(self, pivotX, pivotY, numSelections, selectDirection, moveDirection):
        # Allows us to make the array of marbles to be move much easier
        if selectDirection == 0:
            toAddX = 1
            toAddY = 1
        elif selectDirection == 1:
            toAddX = 2
            toAddY = 0
        elif selectDirection == 2:
            toAddX = 1
            toAddY = -1
        elif selectDirection == 3:
            toAddX = -1
            toAddY = -1
        elif selectDirection == 4:
            toAddX = -2
            toAddY = 0
        else:
            toAddX = -1
            toAddY = 1

        # Puts each marble that will be moved into an array
        for i in range(0, numSelections - 1):
            toMove[i] = [pivotX + (i * toAddX), pivotY + (i * toAddY)]

        # Checks to make sure that each marble is theirs and that they are all in the playing feild
        for i in range(0, numSelections - 1):
            if board[toMove[i][0]][toMove[i][1]] != turn:
                return false
