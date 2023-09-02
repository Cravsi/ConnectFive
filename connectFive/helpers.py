import time
import json
from pathlib import Path
from colorama import Fore, Back, Style

dbFile = Path('./db/savedGames.db')

screens_data = []
with open('./data/menu_screens.json') as file_object:
    screens_data = json.load(file_object)


def validateInput(type, prompt):
    validInput = False
    output = 0

    while not validInput:
        userInput = input(prompt)

        if userInput == '':
            print('+    Input cannot be blank.')
            continue

        match type:
            case 'string':
                try:
                    output = str(userInput)
                except:
                    print('+    Please input a string value.')
                    continue

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


def printToCLI(component):
    fore = Fore.BLUE
    back = Back.WHITE
    reset = Style.RESET_ALL
    graphic = screens_data.get(component, [])
    for line in graphic:
        print(back + fore + line + reset)
        time.sleep(0.16)
