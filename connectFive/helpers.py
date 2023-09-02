import time
import json
from pathlib import Path
from colorama import Fore, Back, Style

fore = Fore.BLUE
back = Back.WHITE
reset = Style.RESET_ALL

dbFile = Path('./db/savedGames.db')

screens_data = []
with open('./data/menu_screens.json') as file_object:
    screens_data = json.load(file_object)


def validateInput(type, prompt):
    validInput = False
    output = 0

    while not validInput:
        userInput = input(back + fore + prompt + reset)

        if userInput == '':
            printStrToCLI('+    Input cannot be blank.')
            continue

        match type:
            case 'string':
                try:
                    output = str(userInput)
                except:
                    printStrToCLI('+    Please input a string value.')
                    continue

            case 'int':
                try:
                    output = int(userInput)
                    validInput = True
                except:
                    printStrToCLI('+    Please input an integer.')
                    continue

            case 'bool':
                if userInput not in ['y', 'Y', 'n', 'Y']:
                    printStrToCLI('+    Please input an Y or N.')
                    continue

                if userInput in ['y', 'Y']:
                    output = True
                    validInput = True
                elif userInput in ['n', 'N']:
                    output = False
                    validInput = True
                else:
                    printStrToCLI('+    Unknown error, please try again')
                    continue
        return output


def printCompToCLI(component):
    graphic = screens_data.get(component, [])
    for line in graphic:
        print(back + fore + line + reset)
        time.sleep(0.04)


def printStrToCLI(string):
    time.sleep(0.04)
    print(back + fore + string + reset)
