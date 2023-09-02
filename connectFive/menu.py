from connectFive.game import Game
from connectFive.helpers import printCompToCLI, validateInput
from connectFive.dataHandler import loadGame


def openingGraphics():
    printCompToCLI("intro")


def openMenu():
    exiting = False

    while not exiting:
        printCompToCLI("main_menu")
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
