import openai
import subprocess
import os

# Uzupełnij swoje dane dotyczące API OpenAI
openai.api_key = "your_openai_api_key"

def process_response(response):
    command = response.choices[0].text.strip()
    return command

def execute_command(command):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, shell=True)
        return result.stdout
    except Exception as e:
        return str(e)

def main():
    while True:
        query = input("Pytanie: ")
        if query.lower() == "exit":
            break

        prompt = f"Przetłumacz to polecenie na język terminala: {query}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        command = process_response(response)
        print(f"Polecenie: {command}")
        result = execute_command(command)
        print(f"Wynik: {result}")

if __name__ == "__main__":
    main()
