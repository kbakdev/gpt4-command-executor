import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


# get_terminal_command(prompt) -> command
# Description: Generate command to execute
# based on prompt
def get_terminal_command(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=profile_prompt(prompt),
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    command = response.choices[0].text.strip()
    return command

# make prompt a little better, so it prints only the command, not the whole prompt
def profile_prompt(prompt):
#     return string where you ask to print one line command without anymore information, and then you return the command, you can also ask based on your os
    return "print one line command for terminal without anymore information:\n" + prompt + "\ncommand:"

def authorize_api_key():
    openai.api_key = OPENAI_API_KEY
