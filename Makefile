.PHONY: install test clean

install:
	pip install -r requirements.txt

test:
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -r {} +
	find . -name "*.pyc" -exec rm {} +
	find . -name "*.pyo" -exec rm {} +
	find . -name "*~" -exec rm {} +