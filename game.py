class game:

    def __init__(self, setUp, capturedToWin):
        self.setUp = setUp
        self.capturedToWin = capturedToWin
        self.turn = 1
        self.points = [0,0]
        self.board =  [[4,4,4,4,4,3,3,3,3,3,3],
                      [4,4,4,4,3,0,0,0,0,0,3],
                      [4,4,4,3,0,0,0,0,0,0,3],
                      [4,4,3,0,0,0,0,0,0,0,3],
                      [4,3,0,0,0,0,0,0,0,0,3],
                      [3,0,0,0,0,0,0,0,0,0,3],
                      [4,3,0,0,0,0,0,0,0,0,3], 
                      [4,4,3,0,0,0,0,0,0,0,3],
                      [4,4,4,3,0,0,0,0,0,0,3],
                      [4,4,4,4,3,0,0,0,0,0,3],
                      [4,4,4,4,4,3,3,3,3,3,3]]
        #setUpDefault()
        self.board =  [[4,4,4,4,4,3,3,3,3,3,3],
                      [4,4,4,4,3,1,1,1,1,1,3],
                      [4,4,4,3,1,1,1,1,1,1,3],
                      [4,4,3,0,0,1,1,1,0,0,3],
                      [4,3,0,0,0,0,0,0,0,0,3],
                      [3,0,0,0,0,0,0,0,0,0,3],
                      [4,3,0,0,0,0,0,0,0,0,3], 
                      [4,3,3,0,0,2,2,2,0,0,3],
                      [4,3,3,3,2,2,2,2,2,2,3],
                      [4,3,3,3,3,2,2,2,2,2,3]]
    def setUpDefault(self):
        self.board =[[4,4,4,4,4,3,3,3,3,3,3],
                      [4,4,4,4,3,1,1,1,1,1,3],
                      [4,4,4,3,1,1,1,1,1,1,3],
                      [4,4,3,0,0,1,1,1,0,0,3],
                      [4,3,0,0,0,0,0,0,0,0,3],
                      [3,0,0,0,0,0,0,0,0,0,3],
                      [4,3,0,0,0,0,0,0,0,0,3], 
                      [4,4,3,0,0,2,2,2,0,0,3],
                      [4,4,4,3,2,2,2,2,2,2,3],
                      [4,4,4,3,3,2,2,2,2,2,3]]
    def move(self, pivotX, pivotY, numSelections, selectDirection, moveDirection):
        toMove = [[0,0],[0,0],[0,0]]

        # Allows us to make the array of marbles to be move much easier
        if selectDirection == 1:
            toAddX = 0
            toAddY = -1
        elif selectDirection == 2:
            toAddX = 1
            toAddY = -1
        elif selectDirection == 3:
            toAddX = 1
            toAddY = 0
        elif selectDirection == -1:
            toAddX = 0
            toAddY = 1
        elif selectDirection == -2:
            toAddX = -1
            toAddY = -1
        elif selectDirection == -3:
            toAddX = -1
            toAddY = 0
        else:
            return "invaid Selection direction" 

        # Puts each marble that will be moved into an array
        for i in range(0, numSelections):
            toMove[i] = [pivotY + (i * toAddY), pivotX + (i * toAddX)]

        # Changes the toAdd parameters to the move direction
        if moveDirection == 1:
            toAddX = 0
            toAddY = -1
        elif moveDirection == 2:
            toAddX = 1
            toAddY = -1
        elif moveDirection == 3:
            toAddX = 1
            toAddY = 0
        elif moveDirection == -1:
            toAddX = 0
            toAddY = 1
        elif moveDirection == -2:
            toAddX = -1
            toAddY = -1
        elif moveDirection == -3:
            toAddX = -1
            toAddY = 0
        else:
            return "invaid move direction" 

        # Iterates though all of the the current players marbles we are moving
        for i in range(0, numSelections):
            # Checks to make sure that each marble is theirs and that they are all in the playing feild
            if self.board[toMove[i][0]][toMove[i][1]] != self.turn:
                return "invaid selection" 

            # Checks to see if we need to check pushing because you cant push with only 1 piece
            if abs(moveDirection) == abs(selectDirection):
                if self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] == (self.turn % 2) + 1:
                    # If in here we need to check to see if a push needs to happen if not then invaid move by looking at the number of marbles we need to push
                    counter = 0
                    for j in range(1, 4):
                        if self.board[toMove[i][0] + (toAddY * j)][toMove[i][1] + (toAddX * j)] == (self.turn % 2) + 1:
                            counter = counter + 1
                    # This if statment will be true if the push cant happen thus its an invaid move because there is more or the same marbles for the other team
                    if counter >= numSelections:
                        return "invaid push" 
                    # if we are here then we need to Push the other players marbles
                    for j in range(numSelections - 1, 0, -1):
                       self.board[toMove[i][0] + (toAddY * j)][toMove[i][1] + (toAddX * j)] = 0
                       if self.board[toMove[i][0] + (toAddY * (j + 1))][toMove[i][1] + (toAddX * (j + 1))] == 3:
                           self.points[turn - 1] += 1
                       else:
                           self.board[toMove[i][0] + (toAddY * (j + 1))][toMove[i][1] + (toAddX * (j + 1))] = (self.turn % 2) + 1
            else:
                if self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] != 0:
                    return "invaid move" 

            # now that all the pushing is done we just move the marbles
        if selectDirection == -moveDirection:
            for i in range(0, numSelections, 1):
               self.board[toMove[i][0]][toMove[i][1]] = 0
               self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] = self.turn
        else:
            for i in range(numSelections - 1, -1, -1):
               self.board[toMove[i][0]][toMove[i][1]] = 0
               self.board[toMove[i][0] + toAddY][toMove[i][1] + toAddX] = self.turn
            
        #update whos turn it is
        self.turn = (self.turn % 2) + 1
        return self.board

    def getBoard(self):
        return self.board

    def getInput(self):
        print("Input an X postion:")
        x = int(input())
        print("Input a Y postion:")
        y = int(input())
        print("Input the amount of peices to move:")
        num = int(input())
        print("Input Selection direction:")
        sel = int(input())
        print("Input Move direction:")
        move = int(input())
        ret = self.move(x,y,num,sel,move)
        if ret != self.board:
            print(ret)

    def getPoints(self):
        return str(self.points) 

    def getTurn(self):
        return str(self.turn)


# Testing
test = game(1,3)
for x in test.getBoard():
    print(x)
print("Score is: " + test.getPoints())
print("Player " + test.getTurn() + "turn")
while 1 == 1:
    test.getInput()
    print("------------------------")
    for x in test.getBoard():
        print(x)
    print("Score is: " + test.getPoints()) 
    print("Player " + test.getTurn() + "turn")




