import sqlite3
import os
from sqlite3 import Error

def create_connection():
    absolute_path = os.path.dirname(__file__)
    relative_path = "sql/game.db"
    database = os.path.join(absolute_path, relative_path)

    connection = None
    try:
        connection = sqlite3.connect(database)
        print("databse connection established")
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(connection, create_table_sql):
    try:
        cur = connection.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


def setup_db():
    users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """

    leaderboard_table = """CREATE TABLE IF NOT EXISTS leaderboard (
                                    username text NOT NULL,
                                    game TEXT NOT NULL,
                                    wins integer,
                                    losses integer,
                                    user_id integer,
                                    FOREIGN KEY(user_id) REFERENCES users(id)
                                );"""

    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, users_table)

        # create leaderboard table
        create_table(conn, leaderboard_table)
        print("database setup completed")

        conn.close()
        print("database connection closed")
    else:
        print("Error! cannot create the database connection.")

def create_user(username: str, password: str) -> int:
    sql = ''' INSERT INTO users(username, password)
              VALUES(?,?) '''
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (username, password))
        conn.commit()
        print("new User registered in database")

        cur.close()
        
        return cur.lastrowid
    except Error as e:
        print("Error writing new User in database:", e)
    finally:
        if conn:
            conn.close()
            print("databse connection closed")

