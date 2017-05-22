from random import randint
import math

board = []
answerBoard = []
boardSize = 5

for x in range(boardSize):
    board.append(["-"] * boardSize)
    
for x in range(boardSize):
    answerBoard.append(["-"] * boardSize)

def print_board(board):
    for row in board:
        print " ".join(row)

#random row & col & direction
def generateRandomPoint(boardSize):
    return randint(1, boardSize**2)
#find coordinate from point
def findX(point, boardSize):
    if point % boardSize == 0:
        return (point/boardSize)-1
    else:
        return point/boardSize
def findY(point, boardSize):
    if point%boardSize == 0:
        return boardSize-1
    else:
        return (point%boardSize) -1
def randomSize(boardSize):
    return randint(1, boardSize)
def randomDirection():
    direction = randint(0,1)
    if randint(0,1) == 0:
        return "H"
    else: 
        return "V"  
    
def checkValidAndMarkShip(point, size, direction):
    xPos = findX(point, boardSize)
    yPos = findY(point, boardSize)
    if direction == "H":
        #check
        if (yPos + size - 1) < 5:
            # mark if available
            notValid = False
            for j in range(yPos,(yPos + size)):
                if answerBoard[xPos][j] == "O":
                    notValid = True
            if notValid == False:
                for j in range(yPos,(yPos + size)):
                    answerBoard[xPos][j] = "O"  
                return True
        else:
            return False
    elif direction == "V":
        #check
        if (xPos + size - 1) < 5:
            # mark if available
            notValid = False
            for i in range(xPos,(xPos + size)):
                if answerBoard[i][yPos] == "O":
                    notValid = True
            if notValid == False:
                for i in range(xPos,(xPos + size)):
                    answerBoard[i][yPos] = "O"
                return True
        else:
            return False

#create new ship
def createNewShip(size, direction):
    createSuccess = False
    while not createSuccess:
        point = generateRandomPoint(boardSize)
        createSuccess = checkValidAndMarkShip(point, size, direction)
    return point

def checkEndGame(answerBoard, boardSize):
    count = 0
    for i in range(0,boardSize):
        for j in range(0,boardSize):
            if answerBoard[i][j] == "O":
                count += 1              
    return count    

class Ship(object):
    placements = []
    def __init__(self, point, size, direction):
        self.point = point
        self.xPos = findX(point, boardSize)
        self.yPos = findY(point, boardSize)
        self.size = size
        self.direction = direction
    def printInfo(self):
        print "Point: ", self.point
        print "X,Y: ", self.xPos, "," ,self.yPos
        print "Length: ", self.size
        print "Direction: ", self.direction

def clearBoard(board, boardSize):
    for i in range(0,boardSize):
        for j in range(0,boardSize):
            board[i][j] = "-"   

def rounduptofive(x):
    return int(math.ceil(x / 5.0)) * 5
    
def initGame():
    print "Let's play Battleship!"
    playGame()  

def playGame():

    clearBoard(board, boardSize)
    clearBoard(answerBoard, boardSize)
    
    # create a fleet
    fleet = []
    noOfShips = 3

    for i in range(0,noOfShips):
        #create a ship
        randSize = randomSize(boardSize)
        randDirection = randomDirection()
        fleet.append(Ship(createNewShip(randSize,randDirection), randSize, randDirection))
    
    #print "Answer"
    #print_board(answerBoard)
    #print "No. of ship: ", checkEndGame(answerBoard, boardSize)
    
    maxTurns = rounduptofive(checkEndGame(answerBoard, boardSize))
    print "-----------"
    print "Game Start!"
    print "-----------"
    print_board(board)
    print "You have a total of ", maxTurns, " turns.\n"

    for turn in range(1,maxTurns + 1):
        print "Turn", turn,"/", maxTurns
        guess_row = int(raw_input("Guess Row:")) - 1
        guess_col = int(raw_input("Guess Col:")) - 1
        
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean.\n"
                if turn == maxTurns:
                    print "Game Over\n"
                    restartGame()
        else:
            if answerBoard[guess_row][guess_col] == "O":
                if board[guess_row][guess_col] != "-":
                    print "You guessed that one already.\n"
                    if turn == maxTurns:
                        print "Game Over"
                        restartGame()
                else:
                    board[guess_row][guess_col] = "O"
                    print "Attack success!"
                    print_board(board)
                    if checkEndGame(board, boardSize) < checkEndGame(answerBoard, boardSize):
                        leftover = checkEndGame(answerBoard, boardSize) - checkEndGame(board, boardSize)
                        print leftover, "more ships to go.\n"
                        if turn == maxTurns:
                            print "Game Over\n"
                            restartGame()
                    else:
                        print "All ships have sunk. You win!"
                        restartGame()
                    if turn == maxTurns:
                        print "Game Over\n"
                        restartGame()
            else:
                if board[guess_row][guess_col] != "-":
                #(board[guess_row][guess_col] == "O") or (board[guess_row][guess_col] == "X"):
                    print "You guessed that one already.\n"
                    if turn == maxTurns:
                        print "Game Over\n"
                        restartGame()
                else:
                    board[guess_row][guess_col] = "X"
                    print "You missed my battleship!"
                    print_board(board)
                    if checkEndGame(board, boardSize) < checkEndGame(answerBoard, boardSize):
                        leftover = checkEndGame(answerBoard, boardSize) - checkEndGame(board, boardSize)
                        print leftover, "more ships to go.\n"
                    else:
                        print "All ships have sunk. You win!\n"
                        break
                    if turn == maxTurns:
                        print "Game Over\n"
                        restartGame()
                
def restartGame():
    answer = raw_input("Restart?[Y/N]: ")
    if answer == "Y":
        print "\n"
        playGame()
    elif answer == "N":
        print "Bye Bye~\n"
        
initGame()
                
# 2-player game
# statistics