import sqlite3
import json

class StoryDatabaseLoader:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create tables for different story elements
        self.c.execute('''

        ''')
      
        self.conn.commit()

    def load_data(self, filename, table):
        # Load JSON data
        with open(filename) as f:
            data = json.load(f)

        # Insert JSON data into the corresponding table
        for elements, subelement in data.items():
            self.c.execute(f'''
                INSERT INTO {table} (elements, subelement, description)
                VALUES (?, ?, ?)
            ''', (elements, subelement, subelement))
        self.conn.commit()

    def generate_storyline(self):
        # Example query to join data from the three tables
        # This is a simple example and may need to be adjusted based on your specific requirements
        self.c.execute('''
            INSERT INTO Storyline (character_development, world_building, plot)
            SELECT cd.description, wb.description, p.description
            FROM CharacterDevelopment cd, WorldBuilding wb, Plot p
            ORDER BY RANDOM()
            LIMIT 1
        ''')
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Example usage
#db_loader = StoryDatabaseLoader('story_elements.db')
#db_loader.load_data(r'myflaskapp\myflaskapp\story_character_development_elements.json', 'CharacterDevelopment')
#db_loader.load_data(r'myflaskapp\myflaskapp\world_building_elements.json', 'WorldBuilding')
#db_loader.load_data(r'myflaskapp\myflaskapp\plot.json', 'Plot')
#db_loader.close_connection()
  




