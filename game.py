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
        #setUpDefault()
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
        toMove = [[0,0],[0,0],[0,0]]

        # Allows us to make the array of marbles to be move much easier
        if selectDirection == 1:
            toAddX = 1
            toAddY = -1
        elif selectDirection == 2:
            toAddX = 2
            toAddY = 0
        elif selectDirection == 3:
            toAddX = 1
            toAddY = 1
        elif selectDirection == -1:
            toAddX = -1
            toAddY = 1
        elif selectDirection == -2:
            toAddX = -2
            toAddY = 0
        elif selectDirection == -3:
            toAddX = -1
            toAddY = -1
        else:
            return false

        # Puts each marble that will be moved into an array
        for i in range(0, numSelections):
            toMove[i] = [pivotY + (i * toAddY), pivotX + (i * toAddX)]

        # Changes the toAdd parameters to the move direction
        if moveDirection == 1:
            toAddX = 1
            toAddY = -1
        elif moveDirection == 2:
            toAddX = 2
            toAddY = 0
        elif moveDirection == 3:
            toAddX = 1
            toAddY = 1
        elif moveDirection == -1:
            toAddX = -1
            toAddY = 1
        elif moveDirection == -2:
            toAddX = -2
            toAddY = 0
        elif moveDirection == -3:
            toAddX = -1
            toAddY = -1
        else:
            return False

        # Iterates though all of the the current players marbles we are moving
        for i in range(0, numSelections):
            # Checks to make sure that each marble is theirs and that they are all in the playing feild
            if self.board[toMove[i][0]][toMove[i][1]] != self.turn:
                print(toMove)
                return False

            # Checks to see if we need to check pushing because you cant push with only 1 piece
            if abs(moveDirection) == abs(selectDirection):
                if self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] == (self.turn % 2) + 1:
                    # If in here we need to check to see if a push needs to happen if not then invaid move
                    counter = 0
                    for j in range(1, 4):
                        if self.board[toMove[i][0] + (toAddY * j)][toMove[i][1] + (toAddX * j)] == (self.turn % 2) + 1:
                            counter = counter + 1
                    # This if statment will be true if the push cant happen thus its an invaid move
                    if counter < numSelections:
                        return False
                    # if we are here then we need to Push the other players marbles
                    for j in range(numSelections - 1, 0, -1):
                       self.board[toMove[i][0] + (toAddY * (j + 1))][toMove[i][1] + (toAddX * (j + 1))] = (self.turn % 2) + 1
                       self.board[toMove[i][0] + (toAddY * j)][toMove[i][1] + (toAddX * j)] = 0
            else:
                if self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] != 0:
                    return False

        # now that all the pushing is done we just move the marbles
        for i in range(0, numSelections):
           self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] = self.turn
           self.board[toMove[i][0]][toMove[i][1]] = 0

        #update whos turn it is
        self.turn = (self.turn % 2) + 1
        return self.board

    def getBoard(self):
        return self.board





# Testing
test = game(1,3)
#for x in test.getBoard():
    #print(x)
print(test.move(8, 7, 3, 3, -3))

for x in test.getBoard():
    print(x)



