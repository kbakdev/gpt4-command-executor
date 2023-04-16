import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_terminal_command(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    command = response.choices[0].text.strip()
    return command
