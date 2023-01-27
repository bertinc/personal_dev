import sqlite3
import constants as const
import os

class DB:
    """
    Does all the needed database interactions.
    """
    def __init__(self) -> None:
        self.file_path = const.PATH
        self.db_file = os.sep.join([self.file_path, 'timesheet.db'])
        self.sql_file = os.sep.join([self.file_path, 'init_db.sql'])
        self.conn = None

    def close_connection(self):
        """
        Close the connection.
        """
        if self.conn:
            self.conn.close()

    def init_db(self):
        """
        If a DB exists, open it. Else, initialize with the SQL script.
        """
        if not os.path.exists(self.db_file):
            self.init_new_db()

    def init_new_db(self):
        """
        Initialize the database from an SQL script.
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()

            sql_script = open(self.sql_file)
            sql_as_string = sql_script.read()
            cur.executescript(sql_as_string)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()

    def insert_bulk_entries(self, entries):
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()

            query_str = """INSERT INTO entries (date, description, start, duration, notes) VALUES (?, ?, ?, ?, ?)"""
            cur.executemany(query_str, entries)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()