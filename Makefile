install:
	pipenv install

lint:
	pipenv run pylint --recursive=y .

test:
	pipenv run pytest

run:
	pipenv run python day$(DAY)/solution.py
