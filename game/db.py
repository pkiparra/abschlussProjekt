import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    connection = None
    try:
        conn = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"./sql/game.db"

    users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer ORIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """

    leaderboard_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    FOREIGN KEY (user_id) REFERENCES users (id),
                                    username text NOT NULL,
                                    game TEXT NOT NULL,
                                    wins integer,
                                    losses integer
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, users_table)

        # create leaderboard table
        create_table(conn, leaderboard_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
