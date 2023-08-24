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