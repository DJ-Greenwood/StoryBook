

import re
import json
from StoryPackage import StoryBotAI
from StoryPackage import WorldbuildingDatabase

# Now you can use StoryBotAI
bot = StoryBotAI(model="gpt-3.5-turbo-16k-0613")

# Create a StoryDatabase object
# File names for the database and JSON schema
db_name = "StoryDatabase.db"
schema_name = r"combined_json.json"

# Path to the database and JSON schema
db_path_name = r"myflaskapp\StoryPackage\\" + db_name
schema_path_name = r"myflaskapp\StoryPackage\JsonFiles\\" + schema_name

# instance a StoryDatabase object
db = WorldbuildingDatabase(db_path_name, schema_path_name)
#data = db.load_json(schema_path_name)
#db.get_table_names(data)


def load_json(json_path: str):
    """
    Load data from a JSON file and insert it into the database.

    :param json_path: Path to the JSON file.
    """
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data
data = load_json(schema_path_name)

table_names = data['Master List'][0]['properties'][0]['World Building']["ideas"][0].keys()
table_names_keys = data['Master List'][0]['properties'][0]['World Building']["ideas"][0]

aspects = table_names_keys['Plot Elements']['description']

print(aspects['Conflict'])
for name in aspects:
    print(name['Conflict']['Aspect and description'])

