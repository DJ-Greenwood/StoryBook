import os
import json
import re
import requests
import openai
from dotenv import load_dotenv

load_dotenv()
api = os.environ.get('OPENAI_API_KEY')
openai.api_key = api

class Call_AI:
    def __init__(self, model="gpt-3.5-turbo-1106"):
        self.client = openai
        self.model = model

    def read_json_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def get_chatgpt_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt}
                ],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in getting response from ChatGPT: {e}")
            return None

    def extract_image_instructions(self, image_prompt, max_length=500):
        # Enhanced regular expressions
        setting_pattern = r"(in a [^\.,]+|on a [^\.,]+|at the [^\.,]+|inside the [^\.,]+|near a [^\.,]+|beside a [^\.,]+)"
        characters_pattern = r"(a [^\.,]+ man|a [^\.,]+ woman|a [^\.,]+ person|a [^\.,]+ creature|an old [^\.,]+|a young [^\.,]+|a [^\.,]+ child)"
        action_pattern = r"(holding a [^\.,]+|standing [^\.,]+|sitting [^\.,]+|lying [^\.,]+|walking [^\.,]+|running [^\.,]+|jumping [^\.,]+|dancing [^\.,]+)"

        setting = re.search(setting_pattern, image_prompt)
        characters = re.findall(characters_pattern, image_prompt)
        action = re.search(action_pattern, image_prompt)

        instruction_parts = [setting.group() if setting else "", 
                             ", ".join(characters[:]),  
                             action.group() if action else ""]
        instruction = ", ".join(filter(None, instruction_parts))

        if len(instruction) > max_length:
            return instruction[:max_length].rsplit(' ', 1)[0]
        return instruction

    def create_dalle_image(self, dalle_image_prompt):
        try:
            response = self.client.images.generate(
                prompt=dalle_image_prompt,
                n=1,
                size="256x256"
            )
            return response.data[0].url
        except Exception as e:
            print(f"Error in creating image with DALL-E: {e}")
            return None

    def save_to_database(self, cursor, story_info, chat_response, image_url):
        cursor.execute("""
            INSERT INTO stories (story_type, setting, characters, chat_response, image_url)
            VALUES (?, ?, ?, ?, ?)
        """, (story_info['story_type'], story_info['setting'], story_info['characters'], chat_response, image_url))

    def download_image(self, image_url, image_dir):
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(image_dir, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192): 
                f.write(chunk)
