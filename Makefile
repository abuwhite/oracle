# This file is part of Oasis
# https://github.com/znhv/oasis

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2021 Boris Zhenikhov

export PYTHONPATH=bot

install:
	@poetry install
	@poetry build
	python3 -m pip install dist/*.whl --force-reinstall

clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

format: clean
	@poetry run black oasis/ tests/

export:
	@poetry export -f requirements.txt --output requirements.txt

start:
	python3 -m bot

deploy:
	git push heroku main

test:
	#make lint
	make pytest
	make pytest-cov

lint:
	poetry run flake8 bot

pytest:
	poetry run pytest bot tests/

cov-check:
	poetry run pytest --cov=bot tests/

pytest-cov:
	@poetry run pytest --cov=bot --cov-config .coveragerc tests/ -sq --cov-report xml