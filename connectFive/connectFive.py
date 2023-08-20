from colorama import Fore, Back, Style
import time
from connectFive.helpers import validMove

class Game:
    def __init__(self):
        self.turn = 0
        self.board = []
        self.gameOver = False

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
        self.checkForConnect()

        if self.gameOver == True:
            self.endGame()
        else:
            self.turn += 1
            player = 0
            if self.turn % 2 == 0:
                player = 2
            else:
                player = 1

            self.displayBoard(player)
            playerMove = validMove(player, self.board)
            self.insertPlayerMove(playerMove, player)
            

    def endGame(self):
        pass

    def checkForConnect(self):
        pass

    def displayBoard(self, player):
        spacer = '+                                                                                       +'
        print(spacer)
        print('+    Turn: ' + str(self.turn))
        print('+    Player: ' + str(player))
        print(spacer)
        for row in self.board:
            print(f'+                                |  {row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}  {row[5]}  {row[6]}   |                             +')
        print('+                                   _  _  _  _  _  _  _                                 +')
        print('+                                   1  2  3  4  5  6  7                                 +')
        print(spacer)

    def insertPlayerMove(self, playerMove, playerToken):
        for i in  range(len(self.board)):
            column = playerMove - 1
            positionAbove = self.board[i - 1][column]
            position = self.board[i][column]

            # First position
            if i == 5 and position == 0:
                self.board[i][column] = playerToken
                
            # all other positions
            elif position != 0 and positionAbove == 0:
                self.board[i - 1][column] = playerToken

        self.newTurn()    

    def run(self):
        self.openingGraphics()
        self.openMenu()
