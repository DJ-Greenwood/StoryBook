#StoryBotAI.py
__version__ = '1.0.0'
"""
This module defines the OpenAIChatBot class for interacting with OpenAI's APIs.
"""

import os
import json
import re
import requests
from openai import OpenAI
from dotenv import load_dotenv

class StoryBotAI:
    """
    A class to interact with various OpenAI APIs, including ChatGPT and DALL-E.

    Attributes:
        model (str): The model name of GPT (default is "gpt-3.5-turbo-1106").
        api_key (str): API key for general OpenAI services.
        api_key_two (str): Secondary API key for OpenAI services.
        api_key_story_teller (str): API key for story-telling OpenAI services.
        api_key_dalle (str): API key for DALL-E image generation service.
        client_actor_one (OpenAI): OpenAI client configured with `api_key`.
        client_actor_two (OpenAI): OpenAI client configured with `api_key_two`.
        client_story_teller (OpenAI): OpenAI client for story-telling, configured with `api_key_story_teller`.
        client_logic (OpenAI): OpenAI client for logic, configured with `api_key_logic`.
        client_dalle (OpenAI): OpenAI client for DALL-E, configured with `api_key_dalle`.
    """

    def __init__(self, model="gpt-3.5-turbo-16k"):
        """
        Initialize the OpenAIChatBot with a specific GPT model and API keys from environment variables.
        """
        load_dotenv()  # Load environment variables from a .env file
        self.model = model
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.api_key_two = os.environ.get("OPENAI_API_KEY_TWO")
        self.api_key_story_teller = os.environ.get("OPENAI_API_KEY_STORY_TELLER")
        self.api_key_logic = os.environ.get("OPENAI_API_KEY_LOGIC")
        self.api_key_dalle = os.environ.get("OPENAI_API_KEY_DALLE")

        self.client_actor_one = OpenAI(api_key=self.api_key)
        self.client_actor_two = OpenAI(api_key=self.api_key_two)
        self.client_story_teller = OpenAI(api_key=self.api_key_story_teller)
        self.client_dalle = OpenAI(api_key=self.api_key_dalle)

    def get_chatgpt_actor_one(self, system_prompt, prompt):
        """
        Get a response from ChatGPT for the first actor based on the provided prompt.

        Args:
            system_prompt (str): The system prompt to provide context.
            prompt (str): The user prompt for ChatGPT.

        Returns:
            str: The response from ChatGPT, or None if an error occurs.
        """
        try:
            response = self.client_actor_one.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in getting response from ChatGPT: {e}")
            return None

    def get_chatgpt_actor_two(self, system_prompt, prompt):
        """
        Get a response from ChatGPT for the second actor based on the provided prompt.

        Args:
            system_prompt (str): The system prompt to provide context.
            prompt (str): The user prompt for ChatGPT.

        Returns:
            str: The response from ChatGPT, or None if an error occurs.
        """
        try:
            response = self.client_actor_two.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in getting response from ChatGPT: {e}")
            return None

    def get_chatgpt_story_teller(self, system_prompt, prompt):
        """
        Get a response from ChatGPT for story-telling based on the provided prompt.

        Args:
            system_prompt (str): The system prompt to provide context.
            prompt (str): The user prompt for ChatGPT.

        Returns:
            str: The response from ChatGPT, or None if an error occurs.
        """
        try:
            response = self.client_story_teller.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in getting response from ChatGPT: {e}")
            return None
    
    def get_chatgpt_story_teller_continuation(self, prompt):
        """
        Get a response from ChatGPT for story-telling based on the provided prompt.

        Args:
            prompt (str): The user prompt for ChatGPT.

        Returns:
            str: The response from ChatGPT, or None if an error occurs.
        """
        try:
            response = self.client_story_teller.chat.completions.create(
             messages=[
                    {"role": "user", "content": prompt}
                ],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in getting response from ChatGPT: {e}")
            return None
    
    def get_chatgpt_story_logic(self, system_prompt, prompt):
        """
        Get a response from checking the LOGIC of the system.

        Args:
            system_prompt (str): The system prompt to provide context.
            prompt (str): The user prompt for ChatGPT.

        Returns:
            str: The response from ChatGPT, or None if an error occurs.
        """
        try:
            response = self.client_story_teller.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in getting response from ChatGPT: {e}")
            return None

    def create_dalle_image(self, dalle_image_prompt):
        """
        Create an image using DALL-E based on the given prompt.

        Args:
            dalle_image_prompt (str): The prompt for DALL-E to generate an image.

        Returns:
            str: The URL of the generated image, or None if an error occurs.
        """
        try:
            response = self.client_dalle.images.generate(
                prompt=dalle_image_prompt,
                n=1,
                size="256x256"
            )
            return response.data[0].url
        except Exception as e:
            print(f"Error in creating image with DALL-E: {e}")
            return None
        
