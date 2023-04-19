import sqlite3
import os
from sqlite3 import Error
from classes import Difficulty

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
        print("Could not create database connection: ", e)

    return connection

def create_table(connection, create_table_sql):
    try:
        cur = connection.cursor()
        cur.execute(create_table_sql)
        cur.close()
    except Error as e:
        print("Error while checking if table exists / creating database:", e)

def setup_db():
    users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        username text PRIMARY KEY,
                                        password text NOT NULL
                                    ); """

    leaderboard_table = """CREATE TABLE IF NOT EXISTS leaderboard (
                                    username text NOT NULL,
                                    game TEXT NOT NULL,
                                    difficulty TEXT NOT NULL,
                                    wins integer NOT NULL,
                                    losses integer NOT NULL,
                                    FOREIGN KEY(username) REFERENCES users(username)
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

def is_username_available(username: str) -> bool:
    sql = '''SELECT COUNT(*) FROM users WHERE username = ?'''
    print(f'checking in database if username: {username} is available')

    try:   
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (username,))
        conn.commit()
        result = cur.fetchone()
        cur.close()
        if result[0] == 0:
            print("found no match for username")
            return True
        else:
            print("username already exists")
            return False
    except Error as e:
        print("Error while chekcing in db if user already exists:", e)
        return None
    finally:
        if conn:
            conn.close()
            print("database connection closed ")

def create_user(username: str, password: str):
    sql = ''' INSERT INTO users(username, password)
              VALUES(?,?) '''
    print(f'trying to register new user with username {username} in database')        

    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (username, password))
        conn.commit()
        print("new User registered in database")

        cur.close()
    except Error as e:
        print("Error writing new User in database:", e)
    finally:
        if conn:
            conn.close()
            print("databse connection closed")

def get_password_for_user(username: str) -> str:
    sql = '''SELECT password FROM users WHERE username = ? '''
    print(f'Trying to get password for {username} from databse')

    try:   
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (username,))
        conn.commit()
        print("got password from database")
        result = cur.fetchone()
        cur.close()
        if result is not None:
            return result[0]
        else:
            print("could not find password for user in db")
            return None
    except Error as e:
        print("Error while getting password from db:", e)
        return None
    finally:
        if conn:
            conn.close()
            print("database connection closed ")

def user_played_game_before(username: str, game: str, difficulty: Difficulty) -> bool:
    sql = '''SELECT count(*) FROM leaderboard WHERE username = ? and game = ? and difficulty = ?'''
    print(f'Trying to check if {username} played {game} at difficulty {difficulty.value} before in db')

    try:   
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (username, game, difficulty.value))
        conn.commit()
        print("got result from db")
        result = cur.fetchone()
        cur.close()
        print(result[0])
        if result[0]:
            print(f'found entries of {username} playing {game} before')
            return True
        else:
            print(f'found no matching entry of {username} playing {game} before') 
            return False
    except Error as e:
        print("Error while checking if user played game before:", e)
        return None
    finally:
        if conn:
            conn.close()
            print("database connection closed ")

def write_game_result_in_db(username: str, game: str, difficulty: Difficulty, userWon: bool):
    if user_played_game_before(username, game, difficulty):
        if userWon: 
            sql = '''UPDATE leaderboard SET wins = wins + 1 WHERE username = ? and game = ? and difficulty = ?'''
        else:
            sql = '''UPDATE leaderboard SET losses = losses + 1 WHERE username = ? and game = ? and difficulty = ?'''
    else:
        if userWon: 
            sql = '''INSERT INTO leaderboard(username, game, difficulty, wins, losses)
                    Values(?,?,?,1,0)'''
        else:
            sql = '''INSERT INTO leaderboard(username, game, difficulty, wins, losses)
                    Values(?,?,?,0,1)'''
    try:  
        print(f'Trying to update leaderboard for {username} who played {game} at difficulty {difficulty.value} in db') 
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (username, game, difficulty.value))
        conn.commit()
        print("uodated db")
        cur.close()
    except Error as e:
        print("Error while updating leaderboard:", e)
        return None
    finally:
        if conn:
            conn.close()
            print("database connection closed ")

    
def get_leader_board(game: str, difficulty: int) -> list[tuple[str, int, int]]:
    sql = '''SELECT username, wins, losses FROM leaderboard WHERE game = ? and difficulty = ? ORDER BY (wins - losses) DESC'''
    print(f'Trying to get leaderboard for {game} at difficulty {difficulty} from db')

    try:   
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql, (game, difficulty))
        conn.commit()
        print("got result from db")
        result = cur.fetchall()
        cur.close()
        return result
    except Error as e:
        print("Error while getting leaderboard from db", e)
        return None
    finally:
        if conn:
            conn.close()
            print("database connection closed ")