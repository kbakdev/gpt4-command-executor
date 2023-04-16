import gpt4_command_executor
from gpt4_command_executor import execute_command

def main():
    print("Welcome to GPT-4 Command Executor!")
    # authorize API key
    gpt4_command_executor.config.authorize_api_key()
    # get input from user
    prompt = input("Enter your command request (or type 'exit' to quit): ")
    command = gpt4_command_executor.config.get_terminal_command(prompt)
    result = execute_command(command)
    print(f"Command output:\n{result}")

if __name__ == "__main__":
    main()
