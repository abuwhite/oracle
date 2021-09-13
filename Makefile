export PYTHONPATH=bot

start:
	python3 -m bot

test:
	poetry run pytest tests

export:
	poetry export -f requirements.txt --output requirements.txt