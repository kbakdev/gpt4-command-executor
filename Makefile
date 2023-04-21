.PHONY: install test clean

install:
	rm -rf $HOME/.local/bin
	pip install -r requirements.txt
	pip install --user .


test:
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -r {} +
	find . -name "*.pyc" -exec rm {} +
	find . -name "*.pyo" -exec rm {} +
	find . -name "*~" -exec rm {} +

setup_alias_q:
	@alias q='python3 gpt4_command_executor/copilot_cli.py'