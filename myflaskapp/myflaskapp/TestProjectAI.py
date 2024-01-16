
__version__ = "1.0.0"
# TestProjectAI.py

import os
import json
import re
import requests
import sqlite3

from openai import OpenAI
from dotenv import load_dotenv



class JsonDatabaseManager:
    def __init__(self, json_directory, db_path):
        self.json_directory = json_directory
        self.db_path = db_path

    def read_json_files_names(self):
        """
        Read all JSON files in the specified directory.
        """
        data_list = []
        for name in os.listdir(self.json_directory):
            if name.endswith('.json'):
                data_list.append(name)
        return data_list

    def read_json_file(self, json_file_path):
        """
        Reads a JSON file and returns its content.
        """
        with open(json_file_path, 'r') as file:
            return json.load(file)

    def create_database_and_table(self, create_table_sql):
        """
        Creates a SQLite database and a table.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        return cursor, conn

    def insert_data_into_table(self, cursor, data, insert_sql):
        """
        Inserts data into the specified table.
        """
        cursor.executemany(insert_sql, data)

    def run_at_start(self):
        """
        Main method to run at the start.
        """
        file_names = self.read_json_files_names()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        for file_name in file_names:
            json_file_path = os.path.join(self.json_directory, file_name)
            plot_elements_json = self.read_json_file(json_file_path)

            table_name = os.path.splitext(file_name)[0]
            create_table_sql = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                ID INTEGER PRIMARY KEY,
                Aspect TEXT,
                Description TEXT
            );
            '''
            cursor.execute(create_table_sql)

            insert_sql = f'INSERT INTO {table_name} (ID, Aspect, Description) VALUES (?, ?, ?);'
            data_to_insert = []
            for key, values in plot_elements_json['description'][0].items():
                for value in values['Ascpect and description']:
                    data_to_insert.append((value['ID'], value['Aspect'], value['Description']))

            self.insert_data_into_table(cursor, data_to_insert, insert_sql)

        conn.commit()
        cursor.close()
        conn.close()


    def generate_ai_prompt_for_dalle(self, subject, setting, specific_elements, color_scheme, focal_point, style_effect, mood):
        """
        Generates a formatted AI prompt for image generation.

        Args:
            subject (str): Specific subject or scene for the image.
            setting (str): Description of the setting (indoor, outdoor, etc.).
            specific_elements (str): Specific elements to emphasize (lighting, mood, etc.).
            color_scheme (str): Color scheme for the image (vibrant, muted, etc.).
            focal_point (str): Focal point of the image (person, object, etc.).
            style_effect (str): Specific style or effect (depth of field, motion blur, etc.).
            mood (str): Desired mood or emotion for the image.

        Returns:
            str: Formatted string for the AI prompt.
        """
        prompt = (f"Create a photorealistic image that captures {subject} in stunning detail. "
                  f"The setting should be {setting}. There should be a strong emphasis on {specific_elements}. "
                  f"The color palette should be {color_scheme}. The composition should focus on {focal_point}, "
                  f"demonstrating {style_effect}. The overall atmosphere should convey {mood}.")
        return prompt

# Example usage
json_directory = ''
db_path = 'myflaskapp/NewJson/plot_elements.db'
manager = JsonDatabaseManager(json_directory, db_path)

# Generate AI prompt
ai_image_prompt = manager.generate_ai_prompt_for_dalle(
    subject="a serene forest scene",
    setting="outdoor, natural",
    specific_elements="morning light and shadows",
    color_scheme="vibrant greens and earthy browns",
    focal_point="a gently flowing stream",
    style_effect="a realistic and detailed representation",
    mood="peaceful and calming"
)




# Usage Example
#json_directory = 'myflaskapp/Include/NewJson/'
#db_path = 'myflaskapp/Include/NewJson/plot_elements.db'
#manager = JsonDatabaseManager(json_directory, db_path)
#manager.run_at_start()


