from gpt4_command_executor import get_terminal_command, execute_command


def main():
    print("Welcome to GPT-4 Command Executor!")

    while True:
        prompt = input("Enter your command request (or type 'exit' to quit): ")

        if prompt.lower() == "exit":
            break

        # Get a command suggestion from GPT-4
        command = get_terminal_command(prompt)

        print(f"Generated command: {command}")

        # Execute the command (optionally: add a confirmation before execution)
        result = execute_command(command)

        print(f"Command output:\n{result}")


if __name__ == "__main__":
    main()
