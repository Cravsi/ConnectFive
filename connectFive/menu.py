import json
from connectFive.game import Game
from connectFive.helpers import printToCLI, validateInput
from connectFive.dataHandler import loadGame


def openingGraphics():
    printToCLI("intro")


def openMenu():
    exiting = False

    while not exiting:
        printToCLI("main_menu")
        userInput = validateInput(
            'int', '+    Please choose a number from the Menu: ')
        match userInput:
            case 1:
                game = Game()
                game.run()
                openMenu()
            case 2:
                loadGame()

            case 3:
                print('+    Goodbye!')
                unselected = True
                exit()
