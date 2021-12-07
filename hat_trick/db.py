import sqlite3
import os
import constants as const

class DB:
    """
    Does all the needed database intersactions.
    """
    def __init__(self) -> None:
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        self.db_file = f"{self.file_path}\\households.db"
        self.sql_file = f"{self.file_path}\\init_db.sql"
        self.conn = None
        self.exludes = {}
    
    def get_excludes(self, name):
        if name in self.exludes.keys():
            return self.exludes[name]
        else:
            return []

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def init_new_db(self):
        """
        Initialize the database from a script.
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

    def get_names(self, order_by = ''):
        """
        Get a complete list of all names with an optional ORDER BY clause.

        Args:
            order_by (str, optional): Adds an ORDER BY clause to the query. Defaults to ''.

        Returns:
            List: All rows in people table ordered by the optional arg 
        """
        if order_by:
            query = f"SELECT * FROM people WHERE ignore = 0 ORDER BY {order_by}"
        else:
            query = f"SELECT * FROM people WHERE ignore = 0"
        response = []

        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute(query)
            response = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response
    
    def get_households_with_names(self, age = '', gender = ''):
        # build where clause
        where = 'WHERE ignore = 0'
        if age:
            if age == 'adults':
                stage = 1
            if age == 'kids':
                stage = 0
            where += f' AND adult = {stage}'
        if gender:
            where += f' AND gender = \'{gender}\''
        query = f"SELECT first, exclude, household_id FROM people {where} ORDER BY household_id"
        response = {}
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            for row in cur.execute(query):
                # if we haven't seen this household yet, initialize the names list
                if row[const.HOUSEHOLD_ID] not in response.keys():
                    response[row[const.HOUSEHOLD_ID]] = []
                # this means we have excludes to handle
                if row[const.EXCLUDE]:
                    # element = {row[0]: row[1].split('|')}
                    self.exludes[row[const.FIRSTNAME]] = row[const.EXCLUDE].split('|')
                    # response[row[-1]].append(element)
                response[row[const.HOUSEHOLD_ID]].append(row[const.FIRSTNAME])
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response

    def get_unique_households(self):
        # build where clause
        where = 'WHERE ignore = 0'
        query = f"SELECT DISTINCT household_id FROM people {where}"
        response = []
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            for row in cur.execute(query):
                response.append(row[1])
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()
        return response
