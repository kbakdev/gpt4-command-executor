from setuptools import setup, find_packages

setup(
    name="gpt4-command-executor",
    version="0.1",
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