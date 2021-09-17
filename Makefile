export PYTHONPATH=bot

start:
	python3 -m bot

test:
	poetry run pytest tests

deploy:
	git push heroku main

github:
	git push

export:
	poetry export -f requirements.txt --output requirements.txt