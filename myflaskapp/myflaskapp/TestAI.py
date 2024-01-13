
from StoryPackage import StoryBotAI
from StoryPackage import StoryDatabase

# Now you can use StoryBotAI
bot = StoryBotAI(model="gpt-3.5-turbo-1106")


#db = StoryDatabase('myflaskapp\StoryPackage\StoryDatabase.db')


#db.create_table_from_json('myflaskapp\StoryPackage\JsonFiles\story_elements.json')
a = bot.get_chatgpt_actor_one(system_prompt= "you are a master writer that uses dialogue to tell extravagen stories", prompt="write a story for me.")
print(a)