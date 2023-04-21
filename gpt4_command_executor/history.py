import os
import json

HISTORY_FILE = "command_history.json"


def load_command_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)
    return history


def save_command_history(command):
    history = load_command_history()
    history.append(command)

    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)
