import sqlite3
import json
from pathlib import Path
from sqlite3 import Error
from datetime import datetime
from connectFive.helpers import validateInput, printToCLI

dbFile = Path('./db/savedGames.db')

screens_data = []
with open('./data/menu_screens.json') as file_object:
    screens_data = json.load(file_object)


def loadGame():
    from connectFive.game import Game
    saves = []
    if not dbFile.exists():
        print("+    -- No saved games found --")
    else:
        saves = getSavedGames()

    if saves:
        count = 0
        printToCLI("load_menu_top")
        for save in saves:
            count += 1
            turn = save[2]
            name = save[3]
            dtObject = datetime.strptime(save[4], "%Y-%m-%dT%H:%M:%S.%f")
            saveTime = datetime.strftime(dtObject, "%m/%d/%y %I:%M %p")
            print("+                        {}    {}      {}      {}                     +"
                  .format(count, name, turn, saveTime))

        printToCLI("load_menu_bottom")
        userInput = validateInput('int', "+    Please choose a game to load: ")
        try:
            saveChoice = saves[userInput - 1]
            boardString = saveChoice[1]
            saveTurn = saveChoice[2]
            boardArray = json.loads(boardString)
            loadedGame = Game(boardArray, saveTurn)
            loadedGame.run()
        except:
            print("+    -- save does not exist --")


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
    sqlCommand = "SELECT game_id, game_data, turn, save_name, save_date FROM gameData"
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
