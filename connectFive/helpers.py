import sqlite3
import json
from pathlib import Path
from sqlite3 import Error
from datetime import datetime

dbFile = Path('./db/savedGames.db')


def loadGame():
    if not dbFile.exists():
        print("+    -- No saved games found --")

    saves = getSavedGames()
    for save in saves:
        print(save)


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
    print(sqlCommand)
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
