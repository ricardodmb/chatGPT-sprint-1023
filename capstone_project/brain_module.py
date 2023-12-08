#!/usr/bin/python3

import os
import openai
from dotenv import load_dotenv

class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        # self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_key = "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"

        # Set the retrieved API key for the OpenAI library
        openai.api_key = self.api_key

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "You are an expert Python and GO lang expert programmer."

    def request_openai(self, message, role="system"):

        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """

        # Create a chat completion with the provided message and role
        response = openai.chat.completions.create(
            messages=[{"role": role, "content": message}],
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            temperature=0.1,
            n=1,
            # max_tokens=100,
        )

        # Return the message content from the API response
        return response.model_dump()#['choices'][0]['message']['content']
