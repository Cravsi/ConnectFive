def validMove(player, board):
        noValidChoice = True

        while(noValidChoice):
            try:
                playerChoice = int((input(f'+    Your Move Player {player}: ')))
            except:
                print('+    Please input a number')
                continue

            # Check chosen column exists
            if playerChoice not in range(1,8):
                print('+    Please choose a number from the board')
                continue

            # Ensure board can accept move
            if board[0][playerChoice - 1] != 0:
                print('+    This column is full, choose again.')
                continue

            noValidChoice = False
        
        return playerChoice