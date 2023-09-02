import json
from connectFive.helpers import validateInput, printStrToCLI
from connectFive.dataHandler import saveGame
from colorama import Fore, Back, Style


class Game:
    def __init__(self, board=None, turn=None):
        if board == None:
            self.turn = 0
            self.board = []
        else:
            self.turn = turn
            self.board = board

        self.gameOver = False
        self.results = []
        with open('./data/game_screens.json') as file_object:
            self.screens_data = json.load(file_object)

    def newGame(self):
        self.gameOver = False
        self.turn = 0
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
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
            playerMove = self.validMove(player, self.board)

            if playerMove == 'q':
                exit()
            elif playerMove == 's':
                saveName = validateInput(
                    'string', '+    Please name your save: ')
                try:
                    saveGame(self.board, self.turn, saveName)
                except:
                    printStrToCLI('+    Could not save game.')
            else:
                self.insertPlayerMove(playerMove, player)

    def endGame(self):
        player = ''
        if self.turn % 2 == 1:
            player = '1'
        else:
            player = '2'

        gameOverText = self.screens_data["board_peripherals"]["game_over"]
        printStrToCLI(gameOverText)
        printStrToCLI(
            f'+                                      Player {player} Wins                                    +')

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
        boardPeripherals = self.screens_data["board_peripherals"]
        spacer = boardPeripherals["spacer"]
        controlsTop = boardPeripherals["board_controls"]["top"]
        controlsBot = boardPeripherals["board_controls"]["bot"]

        printStrToCLI(spacer)
        if player is not None:
            printStrToCLI(
                f'+    Turn: {str(self.turn).rjust(2)}                                                                           +')
            printStrToCLI('+    Player: ' + str(player) +
                          '                                                                          +')
            printStrToCLI(spacer)

        for row in currentBoard:
            printStrToCLI(
                f'+                                |  {row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}  {row[5]}  {row[6]}   |                             +')
        printStrToCLI(controlsTop)
        printStrToCLI(controlsBot)
        printStrToCLI(spacer)

    def validMove(pself, player, board):
        noValidChoice = True
        playerChoice = 0
        printStrToCLI(
            '+    q = quit, s = save                                                                 +')

        while (noValidChoice):
            try:
                # Needs specific validatation to include 'q' & 's' inputs
                inputStr = f'+    Your Move Player {player}: '
                fore = Fore.BLUE
                back = Back.WHITE
                reset = Style.RESET_ALL
                playerInput = input(back + fore + inputStr + reset)

                if playerInput == 'q':
                    playerChoice = playerInput
                elif playerInput == 's':
                    playerChoice = playerInput
                else:
                    playerChoice = int(playerInput)

                    # Check chosen column exists
                    if playerChoice not in range(1, 8):
                        printStrToCLI(
                            '+    Please choose a number from the board: ')
                        continue

                    # Ensure board can accept move
                    if board[0][playerChoice - 1] != 0:
                        printStrToCLI(
                            '+    This column is full, choose again.')
                        continue

            except:
                printStrToCLI('+    Please input a number')
                continue

            noValidChoice = False

        return playerChoice

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
        if self.turn == 0:
            self.newGame()
        else:
            self.newTurn()
