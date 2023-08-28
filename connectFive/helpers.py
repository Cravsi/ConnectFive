import sqlite3
import json
from pathlib import Path
from sqlite3 import Error
from datetime import datetime

dbFile = Path('./db/savedGames.db')


def loadGame():
    pass


def saveGame(board, gameTurn):
    if not dbFile.exists():
        dbFile.parent.mkdir(parents=True, exist_ok=True)
        createDatabase()

    # format data for entry into table
    board_data = json.dumps(board)
    timeNow = datetime.now().isoformat()

    sqlCommand = "INSERT INTO savedGames.gameData (game_data, turn, save_date) VALUES (?, ?, ?)"
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        cur = conn.cursor()
        cur.execute(sqlCommand, (board_data, gameTurn, timeNow))
        conn.commit()
        print('+    Game saved successfully.')
    except sqlite3.Error as e:
        print("Could not save game to database")
        print(e)
    finally:
        conn.close()


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
             save_name  TEXT
             save_date  DATE)
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
