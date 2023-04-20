import os

import openai
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY


def generate_terminal_command(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following natural language command to a terminal command: {prompt}",
        temperature=0.9,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    command = response.choices[0].text.strip()
    return command
