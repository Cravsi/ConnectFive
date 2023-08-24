import json
import time
from colorama import Fore, Back, Style
from connectFive.game import Game
from connectFive.helpers import validateInput


screens_data = []

with open('./data/menu_screens.json') as file_object:
    screens_data = json.load(file_object)

def openingGraphics():
    printToCLI("intro")

def openMenu():      
    exiting = False

    while not exiting:
        printToCLI("main_menu")
        userInput = validateInput('int', '+    Please choose a number from the Menu: ')
        match userInput:
            case 1:
                game = Game()
                game.run()
                openMenu()
            case 2:
                print('+    Feature currently unavailable.')
            case 3:
                print('+    Goodbye!')
                unselected = True
                exit()

def printToCLI(component):
    fore = Fore.BLUE
    back = Back.WHITE
    reset = Style.RESET_ALL
    graphic = screens_data.get(component, [])
    for line in graphic:
        print(back + fore + line + reset)
        time.sleep(0.16)
