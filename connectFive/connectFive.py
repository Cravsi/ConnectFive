from colorama import Fore, Back, Style
import time
from connectFive.helpers import validMove

class Game:
    def __init__(self):
        self.turn = 0
        self.board = []
        self.gameOver = False
        self.results = []

    def openingGraphics(self):
        fore = Fore.BLUE
        back = Back.WHITE
        reset = Style.RESET_ALL
        introGraphic = [
            '-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -',
            '-----------------------------------------------------------------------------------------',
            '+                              |  0  0  0  0  0  0  0  |                                +',
            '+                                                                                       +',
            '+                                                                                       +',
            '+                                         CONNECT                                       +',
            '+                                          FIVE                                         +',
            '+                                                                                       +',
            '+                                                                                       +',
            '+                              |  0  0  0  0  0  0  0  |                                +',
            '-----------------------------------------------------------------------------------------',
            '-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -'
        ]
        for line in introGraphic:
            print(back + fore + line + reset)
            time.sleep(0.16)

    def openMenu(self):
        print('Menu')
        print('New Game, press 1')
        print('Saved Game, print 2 (coming soon):')
        userMenuChoice = input('Your choice:')
        self.newGame()

    def newGame(self):
        self.gameOver = False
        self.turn = 0
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        self.newTurn()
        

    def newTurn(self):
        self.gameOver = self.checkForConnect()

        if self.gameOver == True:
            self.endGame()
        else:
            self.turn += 1
            player = 0
            if self.turn % 2 == 0:
                player = 2
            else:
                player = 1

            self.displayBoard(player, self.board)
            playerMove = validMove(player, self.board)
            self.insertPlayerMove(playerMove, player)
            

    def endGame(self):
        player = ''
        if self.turn % 2 == 1:
            player = '1'
        else:
            player = '2'

        print('+                                        GAME OVER                                      +')
        print(f'+                                      Player {player} Wins                                    +')
        
        self.displayBoard(None, self.finalBoard)

    def checkForConnect(self):
        width = len(self.board[0])
        height = len(self.board)

        # check vertical
        for row in range(height - 3):
            for col in range(width):
                token = self.board[row][col]
                if token != 0 and self.board[row + 1][col] == token and self.board[row + 2][col] == token and self.board[row + 3][col] == token:
                    self.finalBoard(row, col, 'vertical')
                    return True
                
        # check horizontal
        for row in range(height):
            for col in range(width - 3):
                token = self.board[row][col]
                if token != 0 and self.board[row][col + 1] == token and self.board[row][col + 2] == token and self.board[row][col + 3] == token:
                    self.finalBoard(row, col, 'horizontal')
                    return True
                
        # Check left diagonal /
        for row in range(3, height):
            for col in range(width - 3):
                token = self.board[row][col]
                if token != 0 and self.board[row - 1][col + 1] == token and self.board[row - 2][col + 2] == token and self.board[row - 3][col + 3] == token:
                    self.finalBoard(row, col, 'diagonalRight')
                    return True
                
        # Check right diagonal \
        for row in range(3, height):
            for col in range(3, width):
                token = self.board[row][col]
                if token != 0 and self.board[row - 1][col - 1] == token and self.board[row - 2][col - 2] == token and self.board[row - 3][col - 3] == token:
                    self.finalBoard(row, col, 'diagonalLeft')
                    return True

    def displayBoard(self, player, currentBoard):
        spacer = '+                                                                                       +'
        print(spacer)
        if player is not None:
            print('+    Turn: ' + str(self.turn))
            print('+    Player: ' + str(player))
            print(spacer)

        for row in currentBoard:
            print(f'+                                |  {row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}  {row[5]}  {row[6]}   |                             +')
        print('+                                   _  _  _  _  _  _  _                                 +')
        print('+                                   1  2  3  4  5  6  7                                 +')
        print(spacer)

    def insertPlayerMove(self, playerMove, playerToken):
        placed = False
        i = 0
        while i < len(self.board) and not placed:
            i += 1
            column = playerMove - 1
            positionAbove = self.board[i - 1][column]
            position = self.board[i][column]

            # First position
            if i == 5 and position == 0:
                self.board[i][column] = playerToken
                placed = True
                
            # all other positions
            elif position != 0:
                self.board[i - 1][column] = playerToken
                placed = True

        self.newTurn()    

    def finalBoard(self, row, col, direction):
        self.finalBoard = self.board
        match direction:
            case 'vertical':
                for i in range(4):
                    self.finalBoard[row + i][col] = 'X'

            case 'horizontal':
                for i in range(4):
                    self.finalBoard[row][col + i] = 'X'

            case 'diagonalRight':
                for i in range(4):
                    self.finalBoard[row - i][col + i] = 'X'

            case 'diagonalLeft':
                for i in range(4):
                    self.finalBoard[row - i][col - i] = 'X'
        

    def run(self):
        self.openingGraphics()
        self.openMenu()
