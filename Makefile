PYTHONPATH=$(shell pwd)
export PYTHONPATH


all:

check: flake pytest run-simple

flake:
	python3 -m flake8

pytest:
	coverage erase
	coverage run --branch -m pytest -v -s tests
	coverage report
	coverage html

run-simple:
	python3 examples/simple.py
