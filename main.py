import os
import sqlite3


def start():
    os.system("clear")
    print("""
    SPELLING GAME v0.1.1
    ©Team Name 1    
    Login Status: Not Logged In...
    Please press 1 to Sign Up
    """)
    choice=input("or 2 to Login In: ")
    if choice == "1":
        sign_up(db, cursor)
    elif choice == "2":
        login()
    else:
        print("Not a correct choice, please try again...")
        start()

def sign_up(db, cursor):
    os.system("clear")
    username = ("Please enter your username: ")
    cursor.execute('''SELECT username FROM users WHERE username=?''', (username,))
    selection = cursor.fetchone()
    print(selection)

db = sqlite3.connect('users.db')
cursor = db.cursor()
try:
    cursor.execute('''
                  CREATE TABLE IF NOT EXISTS
                  users
                  (user_id INTEGER PRIMARY KEY, 
                  username TEXT, 
                  first_name TEXT,
                  age INTEGER
                  score INTEGER)
                  ''')
except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
start()