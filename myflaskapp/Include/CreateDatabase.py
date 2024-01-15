
import os
import json
import sqlite3

db_path = 'myflaskapp/Include/NewJson/plot_elements.db'

def read_json_files_names(json_file_directory):
    """
    Read all JSON files in the specified directory.
    
    :param json_file_directory: Path to the directory containing JSON files.
    :return: A list of data from all JSON files.
    """
    data_list = []
    for name in os.listdir(json_file_directory):
        if name.endswith('.json'):
            data_list.append(name)
    return data_list

def read_json_file(json_file_path):
    """
    Reads a JSON file and returns its content.

    :param json_file_path: Path to the JSON file
    :return: Content of the JSON file
    """
    with open(json_file_path, 'r') as file:
        return json.load(file)
    

def create_database_and_table(db_path, create_table_sql):
    """
    Creates a SQLite database and a table.

    :param db_path: Path to the SQLite database file
    :param create_table_sql: SQL statement for creating the table
    :return: Cursor and connection to the database
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    return cursor, conn

def insert_data_into_table(cursor, data, insert_sql):
    """
    Inserts data into the specified table.

    :param cursor: Database cursor
    :param data: Data to be inserted
    :param insert_sql: SQL statement for inserting data
    """
    cursor.executemany(insert_sql, data)
        # Create database and cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

def execute_sql_file(db_path, sql_file_path):
    with sqlite3.connect(db_path) as conn:
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()
        conn.executescript(sql_script)

    # Define paths
    #db_path = 'myflaskapp/Include/NewJson/plot_elements.db'
    #sql_file_path = 'path/to/combine_tables.sql'

# Execute the SQL file
#execute_sql_file(db_path, sql_file_path)

# Define paths
db_path = 'myflaskapp/Include/NewJson/plot_elements.db'
sql_file_path = 'path/to/combine_tables.sql'

def RunAtStart():
    json_directory = 'myflaskapp/Include/NewJson/'
    db_path = 'myflaskapp/Include/NewJson/plot_elements.db'
    
    # Get the list of JSON file names
    file_names = read_json_files_names(json_directory)

    # Create database and cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for file_name in file_names:
        json_file_path = os.path.join(json_directory, file_name)
        plot_elements_json = read_json_file(json_file_path)

        # Table name derived from JSON file name
        table_name = os.path.splitext(file_name)[0]

        # SQL to create a table specific to the JSON file
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            ID INTEGER PRIMARY KEY,
            Aspect TEXT,
            Description TEXT
        );
        '''
        cursor.execute(create_table_sql)

        # Prepare data for insertion
        insert_sql = f'INSERT INTO {table_name} (ID, Aspect, Description) VALUES (?, ?, ?);'
        data_to_insert = []
        for key, values in plot_elements_json['description'][0].items():
            for value in values['Ascpect and description']:
                data_to_insert.append((value['ID'], value['Aspect'], value['Description']))

        # Insert data into the table
        insert_data_into_table(cursor, data_to_insert, insert_sql)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()





