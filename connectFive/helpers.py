import sqlite3
from pathlib import Path
from sqlite3 import Error

dbFile = Path('./db/savedGames.db')


def loadGame():
    pass


def saveGame(board):
    if not dbFile.exists():
        dbFile.parent.mkdir(parents=True, exist_ok=True)
        createDatabase()


def createDatabase():
    """ Create an sqlite database connection """
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print('+    No database found. Sqlite3 database created v.' + sqlite3.version)
        createTable()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def createTable():
    sqlCommand = """
        CREATE TABLE [IF NOT EXISTS] savedGames.gameData (
               game_id  INTEGER PRIMARY KEY,
            date_saved  TEXT,
                  turn  INTEGER,
             save_name  TEXT
        )
"""
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
    cur.execute(sqlCommand)
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
