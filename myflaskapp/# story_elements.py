# story_elements.py
import sqlite3
import json

def create_table_and_insert_data(StoryElements):
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('story_elements.db')
    c = conn.cursor()

    # Create table
    c.execute('''
        CREATE TABLE IF NOT EXISTS StoryElements (
            id INTEGER PRIMARY KEY,
            element TEXT,
            subelement TEXT,
            description TEXT
        )
    ''')

    # Load JSON data
    with open('story_character_development_elements.json') as f:
        data = json.load(f)

    # Insert JSON data into the table
    for element, subelements in data.items():
        for subelement, description in subelements.items():
            c.execute('''
                INSERT INTO StoryElements (element, subelement, description)
                VALUES (?, ?, ?)
            ''', (element, subelement, description))

    # Commit changes and close connection
    conn.commit()
    conn.close()

create_table_and_insert_data()