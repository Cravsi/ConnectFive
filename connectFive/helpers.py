def validateInput(type, prompt):
    validInput = False
    output = 0

    while not validInput:
        userInput = input(prompt)

        if userInput == '':
            print('+    Input cannot be blank.')
            continue 

        match type:
            case 'int':
                try:
                    output = int(userInput)
                    validInput = True
                except:
                    print('+    Please input an integer.')
                    continue
            
            case 'bool':
                if userInput not in ['y', 'Y', 'n', 'Y']:
                    print('+    Please input an Y or N.')
                    continue

                if userInput in ['y', 'Y']:
                    output = True
                    validInput = True
                elif userInput in ['n', 'N']:
                    output = False
                    validInput = True
                else: 
                    print('+    Unknown error, please try again')
                    continue
        return output

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