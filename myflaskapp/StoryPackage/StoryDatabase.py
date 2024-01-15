import json
import sqlite3

class WorldbuildingDatabase:
    """
    A class to manage a worldbuilding database, handling the creation of tables,
    loading data from JSON, and providing CRUD operations.
    """

    def __init__(self, db_path, data):
        """
        Initialize the database connection and create tables.
        
        :param db_path: Path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.data = data
        self.table_name = self.get_table_names(data)
        self.create_database_tables(self.table_name)
        

    def get_table_names(self, data: dict):
        """
        Get the table names from the JSON data.

        :param data: Data loaded from the JSON file.
        :return: List of table names.
        """
        for key in data:
            table_name = key
        return table_name
  
    def create_database_tables(self, table_name):
        """
        Create tables in the database for different worldbuilding elements.
        """
        
        # Example for 'Plot Elements' table
        self.conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    ID INTEGER PRIMARY KEY,
                    Aspect TEXT,
                    Description TEXT
                );
            ''')
        
    def parse_and_insert(self, data, table_name):
        """
        Parse the JSON data and insert it into the corresponding tables.

        :param data: Data loaded from the JSON file.
        """
        # Example for inserting plot elements
        for element in data["Master List"]["World building"][f"{table_name}"]:
            for conflict in element["Conflict"]:
                self.conn.execute(f'INSERT INTO "{table_name}" (ID, Aspect, Description) VALUES (?, ?, ?)',
                                  (conflict["ID"], conflict["Aspect"], conflict["Description"]))
        # ... parsing and inserting for other categories

        self.conn.commit()

    def query_data(self, table_name, condition=None):
        """
        Query data from a specific table with an optional condition.

        :param table: Name of the table to query.
        :param condition: Optional SQL condition for querying.
        :return: Query results.
        """
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, set_statement, condition):
        """
        Update data in a specific table.

        :param table: Name of the table to update.
        :param set_statement: SQL SET statement.
        :param condition: SQL condition for updating.
        """
        query = f"UPDATE {table_name} SET {set_statement} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, condition):
        """
        Delete data from a specific table based on a condition.

        :param table: Name of the table to delete from.
        :param condition: SQL condition for deletion.
        """
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()
