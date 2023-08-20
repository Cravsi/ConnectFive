from colorama import Fore, Back, Style
import time

class Game:
    def __init__(self):
        pass

    def openingGraphics(self):
        fore = Fore.BLUE
        back = Back.WHITE
        reset = Style.RESET_ALL
        introGraphic = [
            '-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -',
            '-----------------------------------------------------------------------------------------',
            '+                                                                                       +',
            '+                                                                                       +',
            '+                                         CONNECT                                       +',
            '+                                          FIVE                                         +',
            '+                                                                                       +',
            '+                                                                                       +',
            '-----------------------------------------------------------------------------------------',
            '-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  -'
        ]
        for line in introGraphic:
            print(back + fore + line + reset)
            time.sleep(0.16)

    def openMenu(self):
        print('Menu')
        print('New Game, press 1')
        print('Saved Game, print 2 (coming soon):')
        userMenuChoice = input('Your choice:')

    def newGame(self):
        pass

    def newTurn(self):
        pass

    def endGam(seld):
        pass

    def run(self):
        self.openingGraphics()
        self.openMenu()
