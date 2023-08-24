import json
import time
from colorama import Fore, Back, Style
from connectFive.game import Game


screens_data = []

with open('./data/menu_screens.json') as file_object:
    screens_data = json.load(file_object)

def openingGraphics():
    printToCLI("intro")

def openMenu():      
    printToCLI("main_menu")

def printToCLI(component):
    fore = Fore.BLUE
    back = Back.WHITE
    reset = Style.RESET_ALL
    graphic = screens_data.get(component, [])
    for line in graphic:
        print(back + fore + line + reset)
        time.sleep(0.16)
