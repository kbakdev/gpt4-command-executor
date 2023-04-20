#!/usr/bin/env python3

import sys
from gpt4_command_executor import config
from gpt4_command_executor import executor


def copilot_cli(prompt):
    command = config.get_terminal_command(prompt)
    return executor.execute_command(command)


def main():
    if len(sys.argv) < 2:
        print("Usage: copilot_cli.py 'command request'")
        sys.exit(1)

    prompt = sys.argv[1]
    result = copilot_cli(prompt)

    if result is not None:
        print(result)
    else:
        print("Sorry, I couldn't generate a command for that request.")


if __name__ == "__main__":
    main()
