import sqlite3
import json
import time
from pathlib import Path
from sqlite3 import Error
from datetime import datetime
from colorama import Fore, Back, Style

dbFile = Path('./db/savedGames.db')

screens_data = []
with open('./data/menu_screens.json') as file_object:
    screens_data = json.load(file_object)

print(screens_data)
