__version__ = "1.0.0"

import sqlite3
import json

class StoryDatabase:
    """
    A class to handle SQLite database operations for story data.
    """

    def __init__(self, db_file_path):
        """
        Initializes the StoryDatabase object with the given database file path.
        """
        self.db_file_path = db_file_path

    def create_table_from_json(self, json_file_path):
        """
        Creates tables in the database based on the structure defined in a JSON file.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            with open(json_file_path, 'r') as file:
                data = json.load(file)
            
            for category, aspects in data.items():
                table_name = category.replace(" ", "_").replace("-", "_")
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (ID INTEGER PRIMARY KEY, Aspect TEXT, Description TEXT)")
                for aspect in aspects:
                    cursor.execute(f"INSERT INTO {table_name} (ID, Aspect, Description) VALUES (?, ?, ?)", 
                                   (aspect['ID'], aspect['Aspect'], aspect['Description']))

            conn.commit()

    def insert_data(self, table_name, id, aspect, description):
        """
        Inserts a new row into the specified table.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO {table_name} (ID, Aspect, Description) VALUES (?, ?, ?)", (id, aspect, description))
            conn.commit()

    def delete_data(self, table_name, id):
        """
        Deletes a row from the specified table based on ID.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM {table_name} WHERE ID = ?", (id,))
            conn.commit()

    def update_data(self, table_name, id, aspect, description):
        """
        Updates a row in the specified table based on ID.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE {table_name} SET Aspect = ?, Description = ? WHERE ID = ?", (aspect, description, id))
            conn.commit()

    def get_table_names(self):
        """
        Retrieves the names of all tables in the database.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            return [table[0] for table in tables]

    def get_column_names(self, table_name):
        """
        Retrieves the column names of the specified table.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            return [column[1] for column in columns]

    def drop_table(self, table_name):
        """
        Drops the specified table from the database.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            conn.commit()

    def search_data(self, table_name, search_query):
        """
        Searches for rows in the specified table that match the search query in their description.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {table_name} WHERE Description LIKE ?", ('%' + search_query + '%',))
            results = cursor.fetchall()
            return results

    def get_all_data(self, table_name):
        """
        Retrieves all rows from the specified table.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {table_name}")
            results = cursor.fetchall()
            return results
    
    def close_database(self):
        """
        Closes the database connection.
        """
        with sqlite3.connect(self.db_file_path) as conn:
            conn.close()

# Example usage:
# db = StoryDatabase('your_database.db')    
# db.create_table_from_json('plot_elements.json')       
# db.insert_data('Plot', 1, 'Beginning', 'The beginning of the story.')
# db.delete_data('Plot', 1)
# db.update_data('Plot', 1, 'Beginning', 'The beginning of the story.')
# print(db.get_table_names())
# print(db.get_column_names('Plot'))
# db.drop_table('Plot')
# print(db.search_data('Plot', 'story'))
# print(db.get_all_data('Plot'))
# db.close_database()