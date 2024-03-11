"""To make doing database operations easier"""
import sqlite3
import os
import constants as const

class TimesheetDB:
    """
    Does all the needed database interactions.
    """
    def __init__(self) -> None:
        self.file_path = const.PATH
        self.db_file = os.sep.join([self.file_path, 'timesheet.db'])
        self.sql_file = os.sep.join([self.file_path, 'init_timesheet_db.sql'])
        self.conn = None
        self.categories = []
        self.valid_categories = []

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
        self.set_categories()

    def init_new_db(self):
        """
        Initialize the database from an SQL script.
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()

            # init db via script
            with open(self.sql_file, encoding='utf-8') as sql_script:
                sql_as_string = sql_script.read()
                cur.executescript(sql_as_string)
            self.conn.commit()

        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()

    def insert_bulk_entries(self, entries):
        """
        Make a build insert of timesheet entries into the database
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()

            query_str = """INSERT INTO dt_entry (date, category, description, start, duration, notes) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.executemany(query_str, entries)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()

    def set_categories(self):
        """
        Sets the categories member variable based on what is in the DB on init
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()

            query_str = 'SELECT category, description FROM rt_category'
            cur.execute(query_str)
            response = cur.fetchall()

            self.categories = response

            # clean up response as single list for valid categories
            valid_categories = []
            for entry in response:
                valid_categories.append(entry[0])
            self.valid_categories = valid_categories

        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response

    def get_report_between(self, start, end):
        """
        Get all entries between the provided start and end dates
        Note: BETWEEN is inclusive of start and end
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            query_str = f'SELECT * FROM dt_entry WHERE date BETWEEN \'{start}\' AND \'{end}\' ORDER BY date ASC, start ASC'
            cur.execute(query_str)
            response = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response

    def get_report_all(self):
        """
        Selects all entries
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            query_str = 'SELECT * FROM dt_entry ORDER BY date ASC, start ASC'
            cur.execute(query_str)
            response = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response

    def get_hours_by_category(self, start, end):
        """
        Sum hours by category accross date range
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            query_str = f'SELECT category, SUM(duration)/60.0 as hours FROM dt_entry WHERE date BETWEEN \'{start}\' AND \'{end}\' GROUP BY category'
            cur.execute(query_str)
            response = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response
    
    def get_hours_by_day(self, start, end):
        """
        Sum hours by day accross date range
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            query_str = f'SELECT date, SUM(duration)/60.0 as hours FROM dt_entry WHERE date BETWEEN \'{start}\' AND \'{end}\' GROUP BY date'
            cur.execute(query_str)
            response = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response
