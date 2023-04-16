from gpt4_command_executor import config, executor


def main():
    print("Welcome to GPT-4 Command Executor!")

    while True:
        prompt = input("Enter your command request (or type 'exit' to quit): ")

        if prompt.lower() == "exit":
            break

        command = config.get_terminal_command(prompt)

        result = executor.execute_command(command)
        if result:
            print(f"Command output:\n{result}")


if __name__ == "__main__":
    main()
