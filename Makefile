export PYTHONPATH=src

start:
	poetry run bot

test:
	poetry run pytest tests

export:
	poetry export -f requirements.txt --output requirements.txt