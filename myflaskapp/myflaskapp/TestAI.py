
from StoryPackage import StoryBotAI
from StoryPackage import StoryDatabase

# Now you can use StoryBotAI
bot = StoryBotAI(model="gpt-3.5-turbo-1106")

db = StoryDatabase('myflaskapp\StoryPackage\StoryDatabase.db')


db.create_table_from_json('myflaskapp\StoryPackage\JsonFiles\story_elements.json')


