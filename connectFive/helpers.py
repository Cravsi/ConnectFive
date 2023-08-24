def validMove(player, board):
        noValidChoice = True
        playerChoice = 0

        while(noValidChoice):
            try:
                playerInput = input(f'+    Your Move Player {player}: ')
                
                if playerInput == 'q':
                    return playerInput
                else:
                    playerChoice = int(playerInput)

                    # Check chosen column exists
                    if playerChoice not in range(1,8):
                        print('+    Please choose a number from the board')
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