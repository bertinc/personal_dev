import sqlite3
import constants as const
import os

class DB:
    """
    Does all the needed database interactions.
    """
    def __init__(self) -> None:
        self.file_path = const.PATH
        self.db_file = os.sep.join([self.file_path, 'households.db'])
        self.db_schema_init_file = os.sep.join([self.file_path, 'init_db.sql'])
        self.init_households_file = os.sep.join([self.file_path, 'init_households.sql'])
        self.conn = None
        self.exludes = {}

    def get_excludes(self, name = ''):
        """
        If any excludes were set on the database for this name, they are returned
        as a list.

        Args:
            name (str): the name we are checking for

        Returns:
            List: names to exclude from random draw, empty if there are none
        """
        if not name:
            # if no name was provided, just return the whole thing
            # put it in a list for consistancy
            return ['ALL EXCLUDES', len(self.exludes), self.exludes]
        if name in self.exludes.keys():
            return self.exludes[name]
        return []

    def add_exclude(self, name, excludes):
        """
        If you need to add an exclude programatically instead of editing the database
        send a name and a list of names. If the exclude already exists, it will extend it.

        Args:
            name (str): Name with exclusions. Example: 'Gabby'
            excludes (List): List of names to exclude. Example: ['Robert', 'Tori']
        """
        if name in self.exludes.keys():
            self.exludes[name].extend(excludes)
        else:
            self.exludes[name] = excludes

    def close_connection(self):
        """
        Close the connection.
        """
        if self.conn:
            self.conn.close()

    def init_new_db(self):
        """
        Initialize the database from an SQL script.
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()

            with open(self.db_schema_init_file, encoding='utf-8') as sql_script:
                sql_as_string = sql_script.read()
                cur.executescript(sql_as_string)
                self.conn.commit()

            with open(self.init_households_file, encoding='utf-8') as sql_script:
                sql_as_string = sql_script.read()
                cur.executescript(sql_as_string)
                self.conn.commit()
        except sqlite3.Error as exception:
            print(exception)
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
            query = f"SELECT * FROM people WHERE pass = 0 ORDER BY {order_by}"
        else:
            query = "SELECT * FROM people WHERE pass = 0"
        response = []

        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute(query)
            response = cur.fetchall()
        except sqlite3.Error as exception:
            print(exception)
        finally:
            self.close_connection()
        return response

    def get_households_with_names(self, age = '', gender = ''):
        """
        Get the names grouped by household. We can also request a specific gender or age category
        or a combination of the two.

        Args:
            age (str, optional): Accepted values are adults or kids. Defaults to ''.
            gender (str, optional): Accepted values are f or m. Defaults to ''.

        Returns:
            Dictionary: the keys are the households and the values are a list of names in each household
        """
        # build WHERE clause
        where = 'WHERE pass = 0'
        if age:
            if age == 'adults':
                stage = 1
            if age == 'kids':
                stage = 0
            where += f' AND adult = {stage}'
        if gender:
            where += f' AND gender = \'{gender}\''
        query = f"SELECT firstname, excludes, household_id FROM people {where} ORDER BY RANDOM()"
        response = {}
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            for row in cur.execute(query):
                # if we haven't seen this household yet, initialize the names list
                if row[const.HOUSEHOLD_ID] not in response.keys():
                    response[row[const.HOUSEHOLD_ID]] = []
                # this means we have excludes to save for later
                if row[const.EXCLUDE]:
                    self.exludes[row[const.FIRSTNAME]] = row[const.EXCLUDE].split('|')
                response[row[const.HOUSEHOLD_ID]].append(row[const.FIRSTNAME])
        except sqlite3.Error as exception:
            print(exception)
        finally:
            self.close_connection()
        return response

    def get_unique_households(self):
        """
        Get all unique household ids.

        Returns:
            List: all unique household ids
        """
        # build where clause
        where = 'WHERE pass = 0'
        query = f"SELECT DISTINCT household_id FROM people {where}"
        response = []
        try:
            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            for row in cur.execute(query):
                response.append(row[0])
        except sqlite3.Error as exception:
            print(exception)
        finally:
            self.close_connection()
        return response
