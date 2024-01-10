import json
import sqlite3


class StoryDatabase:
    """
    A class to handle operations related to the story elements database.
    """

    def __init__(self, db_path):
        """
        Initialize the database connection and create a cursor.
        :param db_path: Path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def read_json_file(self, file_path):
        """
        Reads a JSON file and returns its content.
        :param file_path: Path to the JSON file.
        :return: Content of the JSON file.
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    def create_database_from_json(self, table, data):
        """
        Creates a database table and its columns based on the keys from the JSON data.
        :param table: Name of the table to be created.
        :param data: JSON data used to define the table columns.
        """
        character_keys, _ = self.get_the_key_value_pairs(data)

        # Creating the table with primary key
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY)')

        # Adding other columns
        for key in character_keys:
            self.cursor.execute(f'ALTER TABLE {table} ADD COLUMN {key} TEXT')

    def insert_data(self, table, data):
        """
        Inserts data into the specified table.
        :param table: Table where the data will be inserted.
        :param data: Data to be inserted.
        """
        character_key, character_value = self.get_the_key_value_pairs(data)

        # Preparing column names and placeholders
        columns = ', '.join(character_key)
        placeholders = ', '.join(['?'] * len(character_key))

        # SQL query
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'

        # Inserting the data
        self.cursor.execute(query, character_value)

    def select_information_from_table(self, table):
        """
        Selects and returns all information from the specified table.
        :param table: Table from which to retrieve the data.
        :return: All data from the table.
        """
        self.cursor.execute(f'SELECT * FROM {table}')
        return self.cursor.fetchall()

    def get_the_key_value_pairs(self, data):
        """
        Extracts key-value pairs from the given data, modifying the keys as needed.
        :param data: Data from which to extract key-value pairs.
        :return: Modified keys and their corresponding values.
        """
        character_key = []
        character_value = []
        for properties in data.values():
            for key, value in properties.items():
                modified_key = key.lower().replace(' ', '_').replace('-', '_').replace(',', '')
                character_key.append(modified_key)
                character_value.append(value)
        return character_key, character_value
    
    def update_data(self, table, data, conditions):
        """
        Updates data in the specified table based on given conditions.
        :param table: Table where the data will be updated.
        :param data: Dictionary of column-value pairs to update.
        :param conditions: Conditions for the update in SQL WHERE format.
        """
        # Preparing column updates
        updates = ', '.join([f"{key} = ?" for key in data.keys()])
        values = list(data.values())

        # SQL query
        query = f'UPDATE {table} SET {updates} WHERE {conditions}'

        # Updating the data
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        """
        Commits changes and closes the database connection.
        """
        self.conn.commit()
        self.conn.close()


# Usage Example
table_name = 'story_development_elements'
db = StoryDatabase('character_database.db')
json_data = db.read_json_file(r'myflaskapp\myflaskapp\story_character_development_elements.json')
db.create_database_from_json(table_name, json_data)
db.insert_data(table_name, json_data)
print(db.select_information_from_table(table_name))

# Updating the data connection to ensure that the changes are saved
# to the database and that the connection is closed.
db.close_connection()


