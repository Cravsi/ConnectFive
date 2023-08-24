import json

class Game:
    def __init__(self):
        self.turn = 0
        self.board = []
        self.gameOver = False
        self.results = []
        with open('./data/game_screens.json') as file_object:
            self.screens_data = json.load(file_object)

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
            self.endGame(False)
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
            self.insertPlayerMove(playerMove, player)
            

    def endGame(self):
        player = ''
        if self.turn % 2 == 1:
            player = '1'
        else:
            player = '2'

        gameOverText = self.screens_data["board_peripherals"]["game_over"]
        print(gameOverText)
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
        boardPeripherals = self.screens_data["board_peripherals"]
        spacer = boardPeripherals["spacer"]  
        controlsTop = boardPeripherals["board_controls"]["top"]
        controlsBot = boardPeripherals["board_controls"]["bot"]

        print(spacer)
        if player is not None:
            print('+    Turn: ' + str(self.turn))
            print('+    Player: ' + str(player))
            print(spacer)

        for row in currentBoard:
            print(f'+                                |  {row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}  {row[5]}  {row[6]}   |                             +')
        print(controlsTop)
        print(controlsBot)
        print(spacer)

    def validMove(pself, player, board):
        noValidChoice = True
        playerChoice = 0

        while(noValidChoice):
            try:
                playerInput = input(f'+    Your Move Player {player}: ')
                
                if playerInput == 'q':
                    playerChoice = playerInput
                else:
                    playerChoice = int(playerInput)

                    # Check chosen column exists
                    if playerChoice not in range(1,8):
                        print('+    Please choose a number from the board: ')
                        continue

                    # Ensure board can accept move
                    if board[0][playerChoice - 1] != 0:
                        print('+    This column is full, choose again.')
                        continue

            except:
                print('+    Please input a number')
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
        self.newGame()
