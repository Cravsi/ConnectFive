def validMove():
        playerChoice = input('+    Your Move:\t')

        if playerChoice not in range(1,8,1):
            print('Please choose a number from the board')
            validMove()
        
        return playerChoice