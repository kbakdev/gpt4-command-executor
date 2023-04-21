from setuptools import setup, find_packages

setup(
    name="gpt4-command-executor",
    version="0.1",
    author="Kacper Bąk",
    author_email="contact@kacperbak.pl",
    description="A package that uses GPT-4 to execute commands",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "q = gpt4_command_executor.copilot_cli:main"
        ]
    },
    install_requires=[
        "openai",
        "python-dotenv"
    ],
)
