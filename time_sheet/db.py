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