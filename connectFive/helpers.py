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


def loadGame():
    saves = []
    if not dbFile.exists():
        print("+    -- No saved games found --")
    else:
        saves = getSavedGames()

    if saves:
        printToCLI("load_menu_top")
        for save in saves:
            dtObject = datetime.strptime(save[3], "%Y-%m-%dT%H:%M:%S.%f")
            saveTime = datetime.strftime(dtObject, "%m/%d/%y %I:%M %p")
            print("+                             {}      {}      {}                     +"
                  .format(save[2], save[1], saveTime))
        printToCLI("load_menu_bottom")


def saveGame(board, gameTurn, saveName):
    if not dbFile.exists():
        dbFile.parent.mkdir(parents=True, exist_ok=True)
        createDatabase()

    # format data for entry into table
    board_data = json.dumps(board)
    timeNow = datetime.now().isoformat()

    sqlCommand = "INSERT INTO gameData (game_data, turn, save_name, save_date) VALUES (?, ?, ?, ?)"
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        cur = conn.cursor()
        cur.execute(sqlCommand, (board_data, gameTurn, saveName, timeNow))
        conn.commit()
        print('+    Game saved successfully.')
    except sqlite3.Error as e:
        print("+    -- Error: Could not save game to database --")
        print(e)
    finally:
        if conn is not None:
            conn.close()


def getSavedGames():
    sqlCommand = "SELECT game_id, turn, save_name, save_date FROM gameData"
    savedGames = []
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        cur = conn.cursor()
        cur.execute(sqlCommand)
        rows = cur.fetchall()

        for row in rows:
            savedGames.append(row)
    except sqlite3.Error as e:
        print("+    -- Error: Could not get saved games --")
        print(e)
    finally:
        if conn is not None:
            conn.close()

    return savedGames


def createDatabase():
    """ Create an sqlite database connection """
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print('+    No database found. Sqlite3 database created v.' + sqlite3.version)
        conn.close()
        createTable()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def createTable():
    sqlCommand = """
        CREATE TABLE IF NOT EXISTS gameData (
            game_id  INTEGER PRIMARY KEY,
            game_data  TEXT,
                turn  INTEGER,
            save_name  TEXT,
            save_date  TEXT
    )
    """
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
    cur.execute(sqlCommand)
    conn.commit()
    conn.close()


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
