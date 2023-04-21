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


def generate_command(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following command request into a shell command: {query}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.9,
    )

    command = response.choices[0].text.strip()
    return command


def revise_command(command):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please revise the following shell command to improve its accuracy: {command}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.9,
    )

    revised_command = response.choices[0].text.strip()
    return revised_command


def generate_explanation(command):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Explain the following shell command in simple terms: {command}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
    )

    explanation = response.choices[0].text.strip()
    return explanation
