#!/usr/bin/env python3
import argparse
import subprocess
from gpt4_command_executor import config
from gpt4_command_executor import executor
from gpt4_command_executor.gpt3 import revise_command, generate_command, generate_explanation
from gpt4_command_executor.history import load_command_history, save_command_history


def copilot_cli(prompt):
    command = config.get_terminal_command(prompt)
    return executor.execute_command(command)


def main():
    parser = argparse.ArgumentParser(description="GPT-4 Command Executor")
    parser.add_argument("-q", "--query", type=str, help="Command request")
    parser.add_argument("-e", "--explain", action="store_true", help="Explain the generated command")
    parser.add_argument("-r", "--revise", action="store_true", help="Revise the generated command")
    parser.add_argument("--history", action="store_true", help="Show command history")

    args = parser.parse_args()

    if args.history:
        history = load_command_history()
        for command in history:
            print(command)
        return

    if not args.query:
        parser.print_help()
        return

    command = generate_command(args.query)
    explanation = generate_explanation(command) if args.explain else ""
    print(f"Generated command: {command}")
    if args.explain:
        print(f"Explanation: {explanation}")

    while True:
        user_input = input("Do you want to execute this command? (y/n/r) for revision: ")

        if user_input.lower() == 'y':
            subprocess.run(command, shell=True)
            save_command_history(command)
            break
        elif user_input.lower() == 'n':
            break
        elif user_input.lower() == 'r':
            command = revise_command(command)
            explanation = generate_explanation(command) if args.explain else ""
            print(f"Revised command: {command}")
            if args.explain:
                print(f"Explanation: {explanation}")
        else:
            print("Invalid input, please enter 'y', 'n', or 'r'.")


if __name__ == "__main__":
    main()
